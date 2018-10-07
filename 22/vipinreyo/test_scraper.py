from packtpub.PacktWebScraper import PacktWebScraper
from packtpub.Notifier import Notifier
from packtpub.PacktBookClaimer import PacktBookClaimer


def main():
    scraper = PacktWebScraper()
    book_details = scraper.get_free_packt_book_details()

    print(book_details)

    notifier = Notifier()
    notifier.send_notification_by_mail(book_details)

    pc = PacktBookClaimer()
    driver = pc.get_chromium_web_driver()
    pc.claim_free_book(driver)


if __name__ == '__main__':
    main()
