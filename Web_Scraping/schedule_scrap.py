import schedule
import time

from using_selenium import scrap

schedule.every(1).minutes.do(scrap)

while True:
    schedule.run_pending()
    time.sleep(1)