from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import pandas as pd

element_list = []
driver_path = "C:/Users/rohit/Downloads/edgedriver_win64/msedgedriver.exe"

options = webdriver.EdgeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--log-level=3") 

service = Service(executable_path=driver_path)
def scrape():
    for page in range(1, 4):
        url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}"

        driver = webdriver.Edge(service=service, options=options)

        driver.get(url)
        time.sleep(2)

        titles = driver.find_elements(By.CLASS_NAME, "title")
        prices = driver.find_elements(By.CLASS_NAME, "price")
        descriptions = driver.find_elements(By.CLASS_NAME, "description")
        ratings = driver.find_elements(By.CLASS_NAME, "ratings")

        for i in range(len(titles)):
            element_list.append(
            [titles[i].text, prices[i].text, descriptions[i].text, ratings[i].text]
        )

        driver.quit()

    df = pd.DataFrame(element_list, columns=["Tilte", "Price", "Description", "Rating"])

    print(df)

scrape()