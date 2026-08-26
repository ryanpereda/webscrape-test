from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from .models import Quote, ScrapeState
from .scraper import scrape_quotes


SCRAPE_INTERVAL = timedelta(hours=6)


def get_quotes():
    scrape_state, created = ScrapeState.objects.get_or_create(
        pk=1
    )

    needs_scrape = (
        scrape_state.last_scraped_at is None
        or timezone.now() - scrape_state.last_scraped_at >= SCRAPE_INTERVAL
    )

    if needs_scrape:
        refresh_quotes(scrape_state)

    quotes = Quote.objects.all().order_by("id")

    return quotes


def refresh_quotes(scrape_state):
    scraped_quotes = scrape_quotes()

    if scraped_quotes is None:
        return False

    with transaction.atomic():
        Quote.objects.all().delete()

        Quote.objects.bulk_create([
            Quote(
                text=quote["text"],
                author=quote["author"],
            )
            for quote in scraped_quotes
        ])

        scrape_state.last_scraped_at = timezone.now()
        scrape_state.save()

    return True