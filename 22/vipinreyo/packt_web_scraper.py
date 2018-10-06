
import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class PacktWebScraper:
    FREE_LEARNING_URL = 'https://www.packtpub.com/packt/offers/free-learning'

    def __init__(self):
        self.packt_user = os.getenv("PACKT_USER")
        self.packt_pwd = os.getenv("PACKT_PWD")
        self.driver = None

    def get_chromium_web_driver(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def get_free_packt_book_details(self):
        page = requests.get(self.FREE_LEARNING_URL)

        soup = BeautifulSoup(page.text, 'html.parser')

