from bs4 import BeautifulSoup
import urllib


class PacktScraper(object):

    def __init__(self):
        filename = "../affiliation_link.txt"
        with open(filename, 'r') as f:
            self.url = f.read().rstrip()
        self.get_info()

    def get_resource(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        driver = webdriver.Firefox()
        driver.get(self.url)
        resource = driver.page_source
        driver.close()
        return resource

    def get_info(self):
        soup = BeautifulSoup(self.get_resource(), "lxml")
        content = soup.find('div', id='content')
        self.info = {}
        self.info['left_time'] = content.find("span", class_="packt-js-countdown").text
        self.info['title'] = " ".join(content.find("div", class_="dotd-title").text.split())
        self.info['img_src'] = content.find(
            "div", class_="dotd-main-book-image float-left").find("img").attrs['src']
        self.info['discription'] = " ".join(content.find("div", class_=None, id=None).text.split())
        return self.info

    def __str__(self):
        return "left_time = " + self.info['left_time'] + "\n" + \
            "title = " + self.info['title'] + "\n" + \
            "img_src = " + self.info['img_src'] + "\n" + \
            "discription = \n" + self.info['discription'] + "\n"

if __name__ == "__main__":
    print(PacktScraper())
