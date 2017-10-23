import schedule, time, datetime
from PacketScraping.PacktScraper import PacktScraper
from PacketScraping.Mailer import Mailer


def make_message(info):
    return "title = " + info['title'] + "\n" + \
        "discription = \n" + info['discription'] + "\n" + \
        "left_time = " + info['left_time'] + "\n"


packt_scraper = PacktScraper()
schedule.every().hour.do(packt_scraper.update_info)

temp_title = ""
while True:
    print("running...")
    schedule.run_pending()
    if packt_scraper.is_valid:
        if not temp_title == packt_scraper.info['title']:
            # send mail
            temp_title = packt_scraper.info['title']
            addr = "wonderfulboyx@gmail.com"
            title = "you can get \"" + packt_scraper.info['title'] + "\""
            msg = make_message(packt_scraper.info)
            Mailer(addr, addr).send(title, msg)
            print("send mail")
    time.sleep(1)
