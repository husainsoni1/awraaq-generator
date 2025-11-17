from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5, landscape, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
from pypdf import PdfReader, PdfWriter, PageObject

# Register fonts
pdfmetrics.registerFont(TTFont("AlKanz", "static/fonts/AL-KANZ.TTF"))
pdfmetrics.registerFont(TTFont("KanzAlMarjaan", "static/fonts/KANZ-AL-MARJAAN.TTF"))

def editor(request):
    return render(request, 'editor.html', {})

@csrf_exempt
def export_pdf(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    text = request.POST.get("html", "").replace("<br>", "\n")
    font = request.POST.get("font", "AlKanz")

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A5)
    c.setFont(font, 14)

    # Write text (simple flow)
    y = 780
    for line in text.splitlines():
        c.drawRightString(400, y, line.strip())  # RTL align to the right margin
        y -= 20
        if y < 50:
            c.showPage()
            c.setFont(font, 14)
            y = 780

    c.save()
    pdf = buffer.getvalue()
    buffer.close()

    resp = HttpResponse(pdf, content_type="application/pdf")
    resp["Content-Disposition"] = "attachment; filename=awraaq_a5.pdf"
    return resp


def impose_booklet_bytes(a5_bytes):
    reader = PdfReader(BytesIO(a5_bytes))
    n = len(reader.pages)
    if n == 0:
        raise ValueError("Empty PDF")

    w = reader.pages[0].mediabox.width
    h = reader.pages[0].mediabox.height
    total = ((n + 3) // 4) * 4

    def get_page(i):
        if 1 <= i <= n:
            return reader.pages[i - 1]
        else:
            return PageObject.create_blank_page(width=w, height=h)

    writer = PdfWriter()
    for i in range(total // 4):
        left = get_page(total - (2 * i))
        right = get_page(1 + (2 * i))
        a4_front = PageObject.create_blank_page(width=2 * w, height=h)
        a4_front.merge_translated_page(left, 0, 0)
        a4_front.merge_translated_page(right, w, 0)
        writer.add_page(a4_front)

        left_b = get_page(2 + (2 * i))
        right_b = get_page(total - 1 - (2 * i))
        a4_back = PageObject.create_blank_page(width=2 * w, height=h)
        a4_back.merge_translated_page(left_b, 0, 0)
        a4_back.merge_translated_page(right_b, w, 0)
        writer.add_page(a4_back)

    buf = BytesIO()
    writer.write(buf)
    return buf.getvalue()


@csrf_exempt
def export_booklet(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    text = request.POST.get("html", "").replace("<br>", "\n")
    font = request.POST.get("font", "AlKanz")

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A5)
    c.setFont(font, 14)

    y = 780
    for line in text.splitlines():
        c.drawRightString(400, y, line.strip())
        y -= 20
        if y < 50:
            c.showPage()
            c.setFont(font, 14)
            y = 780

    c.save()
    a5_pdf = buffer.getvalue()
    buffer.close()

    booklet = impose_booklet_bytes(a5_pdf)

    resp = HttpResponse(booklet, content_type="application/pdf")
    resp["Content-Disposition"] = "attachment; filename=awraaq_booklet_a4.pdf"
    return resp

@csrf_exempt
def export_default(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    fmt = request.GET.get("format", "pdf")  # pdf / docx / booklet
    html = request.POST.get("html", "")

    # Base CSS
    css_text = """
    @page { size: A5; margin: 15mm; }
    @font-face { font-family: 'AlKanz'; src: url('/static/fonts/AL-KANZ.TTF'); }
    @font-face { font-family: 'KanzAlMarjaan'; src: url('/static/fonts/KANZ-AL-MARJAAN.TTF'); }
    body { font-family: 'AlKanz', 'KanzAlMarjaan', serif; direction: rtl; }
    """

    html_doc = f"""
    <!doctype html><html><head><meta charset='utf-8'>
    <style>{css_text}</style></head><body>{html}</body></html>
    """

    # Case 1: PDF
    if fmt == "pdf":
        pdf_bytes = HTML(string=html_doc).write_pdf(stylesheets=[CSS(string=css_text)])
        resp = HttpResponse(pdf_bytes, content_type="application/pdf")
        resp['Content-Disposition'] = 'attachment; filename=awraaq_default.pdf'
        return resp

    # Case 2: Booklet
    elif fmt == "booklet":
        a5_pdf = HTML(string=html_doc).write_pdf(stylesheets=[CSS(string=css_text)])
        booklet_bytes = impose_booklet_bytes(a5_pdf)
        resp = HttpResponse(booklet_bytes, content_type="application/pdf")
        resp['Content-Disposition'] = 'attachment; filename=awraaq_booklet.pdf'
        return resp

    # Case 3: DOCX
    elif fmt == "docx":
        from io import BytesIO
        from docx import Document
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")
        doc = Document()
        for p in soup.find_all("p"):
            doc.add_paragraph(p.get_text())

        buf = BytesIO()
        doc.save(buf)
        resp = HttpResponse(buf.getvalue(),
            content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        resp['Content-Disposition'] = 'attachment; filename=awraaq.docx'
        return resp

    else:
        return JsonResponse({"error": "Unknown format"}, status=400)
