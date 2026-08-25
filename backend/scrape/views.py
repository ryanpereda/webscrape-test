from django.http import JsonResponse
from .scraper import scrape_quotes


def quotes(request):
    scraped_quotes = scrape_quotes()

    if scraped_quotes is None:
        return JsonResponse(
            {
                "error": "Unable to scrape the target website."
            },
            status=502,
        )

    return JsonResponse({
        "quotes": scraped_quotes,
        "count": len(scraped_quotes),
    })