import schedule
import time
import scraping

schedule.every(10).seconds.do(scraping.packet_scraping)

while True:
    schedule.run_pending()
    time.sleep(1)
