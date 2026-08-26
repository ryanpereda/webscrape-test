from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from .models import Quote, ScrapeState, Tag
from .scraper import scrape_quotes


SCRAPE_INTERVAL = timedelta(hours=6)


def get_quotes():
    scrape_state, created = ScrapeState.objects.get_or_create(pk=1)

    needs_scrape = (
        scrape_state.last_scraped_at is None
        or timezone.now() - scrape_state.last_scraped_at >= SCRAPE_INTERVAL
    )

    refreshed = False
    refresh_failed = False

    if needs_scrape:
        refreshed = refresh_quotes(scrape_state)

        if not refreshed:
            refresh_failed = True

    quotes = Quote.objects.prefetch_related("tags").order_by("id")

    return {
        "quotes": quotes,
        "last_scraped_at": scrape_state.last_scraped_at,
        "refreshed": refreshed,
        "refresh_failed": refresh_failed,
    }


def refresh_quotes(scrape_state):
    scraped_quotes = scrape_quotes()

    if not scraped_quotes:
        return False

    with transaction.atomic():
        Quote.objects.all().delete()

        for scraped_quote in scraped_quotes:
            quote = Quote.objects.create(
                text=scraped_quote["text"],
                author=scraped_quote["author"],
            )

            for tag_name in scraped_quote["tags"]:
                tag, created = Tag.objects.get_or_create(
                    name=tag_name
                )

                quote.tags.add(tag)

        scrape_state.last_scraped_at = timezone.now()
        scrape_state.save()

    return True