from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["title", "content"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "django_ckeditor_5"}),
        }