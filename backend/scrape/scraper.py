import requests
from bs4 import BeautifulSoup


BASE_URL = "https://quotes.toscrape.com"


def scrape_quotes(page=1):
    if page == 1:
        url = f"{BASE_URL}/"
    else:
        url = f"{BASE_URL}/page/{page}/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.RequestException as error:
        print(f"Scraping error: {error}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    quote_elements = soup.select(".quote")

    quotes = []

    for quote in quote_elements:
        text_element = quote.select_one(".text")
        author_element = quote.select_one(".author")

        if text_element and author_element:
            quotes.append({
                "text": text_element.get_text(strip=True),
                "author": author_element.get_text(strip=True),
            })

    next_button = soup.select_one("li.next")

    has_next_page = next_button is not None

    return {
        "quotes": quotes,
        "has_next_page": has_next_page,
    }