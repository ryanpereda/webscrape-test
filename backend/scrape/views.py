from django.http import JsonResponse
from .scraper import scrape_quotes


def quotes(request):
    page = request.GET.get("page", 1)

    try:
        page = int(page)

        if page < 1:
            raise ValueError

    except ValueError:
        return JsonResponse(
            {
                "error": "Page must be a positive integer."
            },
            status=400,
        )

    scraped_data = scrape_quotes(page)

    if scraped_data is None:
        return JsonResponse(
            {
                "error": "Unable to scrape the target website."
            },
            status=502,
        )

    return JsonResponse({
        "page": page,
        "quotes": scraped_data["quotes"],
        "has_next_page": scraped_data["has_next_page"],
    })