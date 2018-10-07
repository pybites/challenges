"""This Class is written to show how selenium can be used to automate the login to Packtpub and click 'Claim my book'
But this won't work with Packtpub as their CAPTCHA system gets triggered when browser is run using selenium (headless).
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os


class PacktBookClaimer:
    FREE_LEARNING_URL = 'https://www.packtpub.com/packt/offers/free-learning'

    def __init__(self):
        """
        Constructor
        Checks for the Packet Pub user credentials environment variables, else raises exception
        """
        self.packt_user = os.getenv("PACKT_USER")
        self.packt_pwd = os.getenv("PACKT_PWD")

        if not self.packt_user:
            raise ValueError('Packt user id not found.')

        if not self.packt_pwd:
            raise ValueError('Packt user password not found')

        self.driver = None

    def get_chromium_web_driver(self):
        """
        Helper method to get a Chromium selenium driver.
        :return:
        """
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        return self.driver

    def claim_free_book(self, driver):
        driver.maximize_window()
        driver.get(self.FREE_LEARNING_URL)
        time.sleep(4)
        driver.find_element_by_xpath("//*[@class='login-popup']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[@id='account-bar-form']//input[@id='email']").clear()
        driver.find_element_by_xpath("//div[@id='account-bar-form']//input[@id='email']").send_keys(self.packt_user)
        driver.implicitly_wait(2)
        driver.find_element_by_xpath("//div[@id='account-bar-form']//input[@id='password']").clear()
        driver.find_element_by_xpath("//div[@id='account-bar-form']//input[@id='password']").send_keys(
            self.packt_pwd + Keys.RETURN)
        driver.implicitly_wait(20)
        driver.find_element_by_id('free-learning-claim').click()
        driver.implicitly_wait(10)
        driver.find_element_by_id('account-bar-sign-out').click()
