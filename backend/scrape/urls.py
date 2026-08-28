from django.urls import path

from .views import QuoteListView


urlpatterns = [
    path("quotes/", QuoteListView.as_view(), name="quote-list"),
]