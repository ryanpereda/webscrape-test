from django.http import JsonResponse
from .scraper import scrape_quotes


def quotes(request):
    scraped_quotes = scrape_quotes()

    return JsonResponse({
        "quotes": scraped_quotes
    })