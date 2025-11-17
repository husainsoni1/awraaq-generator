from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('editor.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
]
