# Awraaq Generator

A Django-based web application designed to create, edit, and export beautifully formatted **Awraaq**, using **CKEditor 5**, **custom Dawoodi Bohra Lisan-ud-Dawat fonts**, and full **RTL Arabic support**.

This project aims to provide a browser-based alternative to Microsoft Word for producing Dawoodi Bohra community documents using fonts like **Kanz Al Marjaan** and **Al-Kanz**.

---

## 🚀 Features Implemented So Far

### ✔ Fully functional CKEditor 5 integration
- Modern JavaScript rich-text editor
- RTL Arabic support (content direction)
- Custom toolbar configuration
- Font family dropdown with custom fonts

### ✔ Custom Dawoodi Bohra fonts integrated
- **Kanz Al Marjaan** (Unicode-compatible)
- **Al-Kanz** (legacy font; partial Unicode conversion attempt included)
- Fonts loaded through Django static files
- @font-face configured correctly

### ✔ Working Document Model & Forms
- Django ModelForm renders CKEditor 5 widget
- Page to create & save documents
- Document listing page

### ✔ Project Fixes & Cleanup
- Proper Django app structure (`apps.py`, migrations, models)
- Fixed static file system, fonts directory, settings
- Correct CKEditor 5 package installed (`django-ckeditor-5`)
- Removed broken/fake CKEditor packages
- Fixed venv issues
- Added correct `STATIC_ROOT` and collectstatic flow

---

## 🛠️ Project Setup

### 1. Create & activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

2. Install dependencies

If using uv: 
uv sync

Or using pip:
pip install -r requirements.txt

3. Apply migrations
uv run python manage.py migrate

4. Collect static files
uv run python manage.py collectstatic

5. Run the development server
uv run python manage.py runserver


Git 🧑‍💻 Branch Strategy

main:- 

Stable production-like updates.

husainsoni-dev:-

Experimental development branch for:
	•	CKEditor integration
	•	Font testing
	•	Unicode font conversion
	•	UI improvements


📌 Recommended Next Steps (for Husain bhai Vejlani)
	•	Add WeasyPrint PDF export (A5 + booklet imposition)
	•	Add export options (PDF/DOCX/A4 booklet)
	•	Improve UI styling
	•	Add autosave support
	•	Add document editing page
	•	Add controls for margins, line spacing, justification
	•	Continue improving compatibility for Al-Kanz font, currently not working properly on HTML editor


   📝 Commit History Summary
	•	001 – Fixed static fonts path; initial push
	•	002 – README updated
	•	003 – Created husainsoni-dev branch
	•	004 – Saved working state before CKEditor 5 migration
	•	005 – CKEditor5 installed + working; custom fonts + RTL support implemented
   •	006 – Finalized CKEditor5 integration with RTL Arabic, custom fonts, Unicode Al-Kanz patch, and complete README overhaul 
   •	007 – final update readme.md


