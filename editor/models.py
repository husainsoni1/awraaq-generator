from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = CKEditor5Field("Content")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title