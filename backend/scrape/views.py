from django.http import JsonResponse

from .services import get_quotes


def quotes(request):
    data = get_quotes()

    quote_data = [
        {
            "id": quote.id,
            "text": quote.text,
            "author": quote.author,
            "tags": [
                tag.name
                for tag in quote.tags.all()
            ],
        }
        for quote in data["quotes"]
    ]

    return JsonResponse({
        "quotes": quote_data,
        "count": len(quote_data),
        "last_scraped_at": data["last_scraped_at"],
        "refreshed": data["refreshed"],
        "refresh_failed": data["refresh_failed"],
    })