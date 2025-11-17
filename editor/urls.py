from django.urls import path
from . import views

urlpatterns = [
    path('', views.editor, name='editor'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('export/booklet/', views.export_booklet, name='export_booklet'),
    path("export_default/", views.export_default, name="export_default"),
]

