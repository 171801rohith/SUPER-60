import schedule
import time

from using_selenium import scrape

schedule.every(1).minutes.do(scrape)

while True:
    schedule.run_pending()
    time.sleep(1)