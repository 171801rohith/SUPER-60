from Compare import using_selenium
from Compare import using_playwright
import time


def time_taken(pages):
    playwright_start = time.perf_counter()
    using_playwright.scrape(pages)
    playwright_end = time.perf_counter()

    selenium_start = time.perf_counter()
    using_selenium.scrape(pages)
    selenium_end = time.perf_counter()

    selenium_time = selenium_end - selenium_start
    playwright_time = playwright_end - playwright_start

    print("=" * 75)
    print("Time taken by Selenium:", selenium_time)
    print("Time taken by Playwright:", playwright_time)
    print("=" * 75)

    return [playwright_time, selenium_time]
