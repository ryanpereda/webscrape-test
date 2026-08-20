from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_home),
    path("upload/", views.upload_csv),
]