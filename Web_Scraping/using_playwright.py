import time
from playwright.sync_api import sync_playwright
import pandas as pd

element_list = []
def scrape():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()

        for i in range(1, 4):
            url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}"

            page.goto(url)

            page.wait_for_selector(".title")

            titles = page.query_selector_all(".title")
            prices = page.query_selector_all(".price")
            descriptions = page.query_selector_all(".description")
            ratings = page.query_selector_all(".ratings")

            for i in range(len(titles)):
                element_list.append(
                    [
                        titles[i].inner_text() if i < len(titles) else "",
                        prices[i].inner_text() if i < len(prices) else "",
                        descriptions[i].inner_text() if i < len(descriptions) else "",
                        ratings[i].inner_text() if i < len(ratings) else "",
                    ]
                )

    df = pd.DataFrame(element_list, columns=["Tilte", "Price", "Description", "Rating"])

    print(df)


start = time.perf_counter()
scrape()
end = time.perf_counter()

print(end - start)