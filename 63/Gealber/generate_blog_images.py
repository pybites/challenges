from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, URLError
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
import zipfile
import os
import re


class Extractor:
    def __init__(self, headers):
        self.headers = headers

    @staticmethod
    def parser(page, query):
        soup = BeautifulSoup(page, 'lxml')
        items = soup.select(query)
        return items

    def extract_challenge(self):
        url = 'https://codechalleng.es/challenges/'
        request = Request(url, headers=self.headers)
        base_url = 'https://codechalleng.es'
        challenges = {}
        try:
            with urlopen(request) as response:
                html = str(response.read(), 'utf-8')
            items = self.parser(html, "td.challengeTitle > a")
            for item in items:
                link = "".join([base_url, item.get('href')])
                challenges[item.get_text()] = link
        except URLError as error:
            print(error.reason)
        return challenges

    def extract_articles(self):
        url = 'https://pybit.es/pages/articles.html'
        request = Request(url, headers=self.headers)
        articles = {}
        try:
            with urlopen(request) as response:
                html = str(response.read(), 'utf-8')
            items = self.parser(html, "ul.articleList > li > a")
            for item in items:
                link = item.get('href')
                articles[item.get_text()] = link
        except URLError as error:
            print(error.reason)

        return articles


class ImageGenerator:
    def __init__(self, driver_executable):
        self.driver_executable = driver_executable

    @staticmethod
    def fill_form(driver, title: str, url: str):
        try:
            title_element = driver.find_element_by_id("title")
            title_element.send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
            # title_element.send_keys(Keys.BACKSPACE * 15)
            title_element.send_keys(title)
            topoff_select = Select(driver.find_element_by_id("topoffset"))
            time.sleep(1)
            topoff_select.select_by_value("10px")
            theme_select = Select(driver.find_element_by_id("collection"))
            time.sleep(1)
            theme_select.select_by_value("bamboo")
            image_select = driver.find_element_by_id("bg1_url")
            image_select.click()
            time.sleep(5)
            image_select.send_keys(Keys.DOWN * random.randint(1, 25))
            image_select.send_keys(Keys.ENTER)
            overlay_url = driver.find_element_by_id("overlay_url")
            overlay_url.send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
            overlay_url.send_keys(url)
            save = driver.find_element_by_id("btnSave")
            save.click()
            time.sleep(5)
        except Exception as e:
            print(e)

    def generator(self, challenges: dict, articles: dict):
        url = 'http://projects.bobbelderbos.com/featured_image/'
        driver = webdriver.Chrome(executable_path=self.driver_executable)
        driver.get(url)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "blogtitle")))
            width = driver.find_element_by_id("width")
            height = driver.find_element_by_id("height")
            width.send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
            width.send_keys("200")
            height.send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
            height.send_keys("200")
            for title, url in challenges.items():
                self.fill_form(driver, title, url)
                time.sleep(5)
            for title, url in articles.items():
                self.fill_form(driver, title, url)
                time.sleep(5)
        finally:
            driver.close()


def main():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/74.0.3729.169 Safari/537.36"}
    extractor = Extractor(headers=headers)
    image_generator = ImageGenerator("C:\\ChromeDriver\\chromedriver.exe")
    challenges = extractor.extract_challenge()
    articles = extractor.extract_articles()
    image_generator.generator(challenges, articles)
    pattern = re.compile(r'.jpg$')
    download_dir = "C:\\Users\\Gealber\\Downloads"
    with zipfile.ZipFile('download_dir.zip', 'w') as download:
        for file in os.listdir(download_dir):
            if pattern.search(file) is not None:
                download.write(os.path.join(download_dir, file))


if __name__ == '__main__':
    main()
