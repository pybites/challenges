# coding=utf-8 -*-

import requests
from lxml import html

SPLIT_SYMBOLS = [',', ' y ', ' e ', ' - ']


class NameScraper(object):
    """
    Scrapping names for a given url and xpath
    """

    _url: str = None
    _xpath: str = None

    def __init__(self, config):
        self._url = config['url']
        self._xpath = config['xpath']

    def get_names(self) -> list:
        """
        get all found names
        """
        speakers = self.get_items_from_url()
        for symbol in SPLIT_SYMBOLS:
            speakers = self.split_names(speakers, symbol)
        return self.filter_false_names(speakers)

    def get_items_from_url(self) -> list:
        """
        Gets speaker's name list from a web page
        Params:
            url (str): webpage URL to crawl for.
            xpath (str): XPATH to desired items to extract.
        Returns:
            list of str with speaker names or empty list if none
        """
        speakers = list()
        response = requests.get(self._url)
        if response.status_code == requests.codes.ok:
            # import pdb; pdb.set_trace()
            tree = html.fromstring(response.content)
            speakers = tree.xpath(self._xpath)
        return speakers

    def split_names(self, names: list, symbol: str = ',') -> list:
        """
        Some times vairous speakers are published together
        """
        all_names = list()
        for name in names:
            all_names += [_n.strip() for _n in name.split(symbol)]
        return all_names

    def filter_false_names(self, names):
        """
        A name is almost 2 words. A word must contain letters.
        """
        filtered_names = list()
        for name in names:
            are_words = True
            words = name.split()
            for word in words:
                if word.strip().isdigit():
                    are_words = False
                    break
            if len(words) > 1 and are_words:
                filtered_names.append(name)

        return filtered_names
