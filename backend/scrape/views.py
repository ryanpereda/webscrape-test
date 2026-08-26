from django.http import JsonResponse

from .services import get_quotes


def quotes(request):
    quotes = get_quotes()

    quote_data = [
        {
            "text": quote.text,
            "author": quote.author,
        }
        for quote in quotes
    ]

    return JsonResponse({
        "quotes": quote_data,
        "count": len(quote_data),
    })