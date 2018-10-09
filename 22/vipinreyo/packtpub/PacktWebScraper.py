import requests
from bs4 import BeautifulSoup
from datetime import datetime


class PacktWebScraper:
    FREE_LEARNING_URL = 'https://www.packtpub.com/packt/offers/free-learning'

    def __init__(self):
        """
        Constructor
        """
        pass

    def get_free_packt_book_details(self):
        """
        Public method to request, scrape and return the free book details.
        The book details are returned as a dictionary as below
        {
            'title': <Book Title>,
            'description': <Book Description>,
            'time_left': <Time left to claim the book>,
            'cover': <The book cover image source link>
        }
        :return:
        """
        book_details = dict()

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                 ' Chrome/69.0.3497.100 Safari/537.36'}
        page = requests.get(self.FREE_LEARNING_URL, headers=headers)
        page.raise_for_status()

        soup = BeautifulSoup(page.text, 'html.parser')
        book_details['title'] = soup.find(class_="dotd-title").find('h2').get_text().strip()
        book_details['description'] = soup.find(class_="dotd-main-book-summary").find_all('div')[2].get_text().strip()
        book_details['time_left'] = self._time_left(soup.find('span', {'class': 'packt-js-countdown'}).
                                                    get('data-countdown-to'))
        book_details['cover'] = soup.find('img', {'class': 'bookimage'}).get('src')
        return book_details

    def _time_left(self, end):
        """
        Helper function to get the time left to clam the free book
        Expects the end time as parameter
        :param end:
        :return:
        """
        dt = datetime.fromtimestamp(int(end))
        time_left = (dt - datetime.now())
        return (f'{int(time_left.seconds/3600)} hours, {int((time_left.seconds%3600)/60)} and '
                f'{int(time_left.seconds%3600%60)} seconds left')

