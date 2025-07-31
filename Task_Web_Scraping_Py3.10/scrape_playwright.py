# body_x_grid_grd -> table id
# body_x_grid_PagerBtnNextPage -> nextbutton id

import sys
import asyncio
import pandas as pd
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright


if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


class Scraper:
    def __init__(self, url):
        self.solicitation_list = []
        self.url = url
        self.columns = None
        self.df = None

    async def scrape(self, pages):
        try:
            async with async_playwright() as pw:
                browser = await pw.chromium.launch(headless=False)
                web_page = await browser.new_page()
                await web_page.goto(self.url)

                for page in range(pages):
                    await web_page.wait_for_selector("#body_x_grid_grd")

                    table = await web_page.query_selector("#body_x_grid_grd")
                    rows = await table.query_selector_all("tr")

                    if self.columns is None:
                        self.columns = [
                            await cell.inner_text()
                            for cell in await rows[0].query_selector_all("th")
                            if await cell.inner_text() != ""
                        ]

                    for i in range(1, len(self.columns)):
                        cells = await rows[i].query_selector_all("td")
                        self.solicitation_list.append(
                            [
                                (
                                    await cell.inner_text()
                                    if await cell.inner_text() != ""
                                    else pd.NA
                                )
                                for cell in cells
                            ]
                        )

                    await web_page.wait_for_selector("#body_x_grid_PagerBtnNextPage")
                    await web_page.click("#body_x_grid_PagerBtnNextPage")

            print(self.solicitation_list)
            print(self.columns)
            self.df = pd.DataFrame(data=self.solicitation_list, columns=self.columns)

            for col in self.columns:
                if col in ["Editing column"]:
                    self.df = self.df.drop(columns=col)

            return self.df

        except Exception as e:
            print("Error:", e)

    def scrape_site(self, pages):
        return asyncio.run(self.scrape(pages))


