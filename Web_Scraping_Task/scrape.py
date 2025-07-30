from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time


# body_x_grid_grd -> table id
# body_x_grid_PagerBtnNextPage -> nextbutton id


class Scraper:
    def __init__(self, url):
        self.solicitation_list = []
        self.driver_path = "C:/Users/rohit/Downloads/edgedriver_win64/msedgedriver.exe"
        self.options = webdriver.EdgeOptions()

        self.service = Service(executable_path=self.driver_path)
        self.url = url
        self.driver = webdriver.Edge(service=self.service, options=self.options)
        self.columns = None
        self.df = None

    def scrape_site(self, pages):
        try:
            self.driver.get(self.url)
            for i in range(0, pages):
                table = self.driver.find_element(By.ID, "body_x_grid_grd")
                rows = table.find_elements(By.TAG_NAME, "tr")

                if self.columns is None:
                    self.columns = [
                        cell.text
                        for cell in rows[0].find_elements(By.TAG_NAME, "th")
                        if cell.text != ""
                    ]

                for i in range(1, len(rows)):
                    cells = rows[i].find_elements(By.TAG_NAME, "td")
                    self.solicitation_list.append(
                        [cell.text for cell in cells if cell.text != ""] + [""]
                    )

                next_page = self.driver.find_element(
                    By.ID, "body_x_grid_PagerBtnNextPage"
                )
                if next_page:
                    next_page.click()
                else:
                    break
                time.sleep(5)

            self.df = pd.DataFrame(
                data=self.solicitation_list,
                columns=self.columns,
            )
            for col in ["Bid Holders List", "eMM ID"]:
                if col in self.df.columns:
                    self.df.drop(columns=col, inplace=True)

            return self.df
        except Exception as e:
            print("Error:", e)
        finally:
            self.driver.quit()

