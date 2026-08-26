import requests
from bs4 import BeautifulSoup


BASE_URL = "https://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    page = 1

    while True:
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

        for quote in quote_elements:
            text_element = quote.select_one(".text")
            author_element = quote.select_one(".author")
            tag_elements = quote.select(".tags .tag")

            if text_element and author_element:
                tags = [
                    tag.get_text(strip=True)
                    for tag in tag_elements
                ]
                all_quotes.append({
                    "text": text_element.get_text(strip=True),
                    "author": author_element.get_text(strip=True),
                    "tags": tags,
                })

        next_button = soup.select_one("li.next")

        if next_button is None:
            break

        page += 1

    return all_quotes