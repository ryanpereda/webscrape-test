import requests
from bs4 import BeautifulSoup


URL = "https://quotes.toscrape.com/"


def scrape_quotes():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Scraping error: {error}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    quote_elements = soup.select(".quote")

    quotes = []

    for quote in quote_elements:
        text = quote.select_one(".text").get_text()
        author = quote.select_one(".author").get_text()

        quotes.append({
            "text": text,
            "author": author,
        })

    return quotes