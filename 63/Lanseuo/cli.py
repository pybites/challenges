import feedparser
import os
import random
import shutil
import time
from selenium.webdriver import Firefox, FirefoxProfile
from selenium.webdriver.firefox.options import Options

DOWNLOADS_PATH = "/".join(os.getcwd().split("/")[:3]) + "/Downloads"
MAX_NUMBER_OF_IMAGES = 10


def main():
    articles = list(scrape_article_titles())
    number_of_articles = min(len(articles), MAX_NUMBER_OF_IMAGES)
    browser = initialize_browser()

    for index, article_title in enumerate(articles):
        if index == MAX_NUMBER_OF_IMAGES:
            break

        print(f"🖼️  Creating image for '{article_title}' ({index + 1}/{number_of_articles}) ...")
        get_featured_image(browser, article_title)

    zip_files()
    browser.close()
    print("😄  Done")


def scrape_article_titles():
    print("📜  Scraping articles ...")
    document = feedparser.parse("https://pybit.es/feeds/all.rss.xml")
    for article in document["entries"]:
        yield article["title"]


def initialize_browser():
    print("🌎  Initializing browser ...")
    opts = Options()
    opts.headless = True

    profile = FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", DOWNLOADS_PATH + "/blog-images")
    profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    profile.set_preference("browser.download.manager.closeWhenDone", False)
    profile.set_preference("browser.download.manager.focusWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/png")

    browser = Firefox(options=opts, firefox_profile=profile)
    browser.get("http://projects.bobbelderbos.com/featured_image")
    return browser


def get_featured_image(browser, title):
    width_input = browser.find_element_by_id("width")
    width_input.send_keys(300)

    height_input = browser.find_element_by_id("height")
    height_input.send_keys(100)

    title_input = browser.find_element_by_id("title")
    title_input.send_keys(title)

    top_offset_select = browser.find_element_by_id("topoffset")
    options = top_offset_select.find_elements_by_tag_name("option")
    for option in options:
        if option.get_attribute("value") == "50px":
            option.click()

    font_select = browser.find_element_by_id("font")
    options = font_select.find_elements_by_tag_name("option")
    for option in options:
        if option.get_attribute("value") == "Merriweather":
            option.click()

    background_theme_select = browser.find_element_by_id("collection")
    options = background_theme_select.find_elements_by_tag_name("option")
    for option in options:
        if option.get_attribute("value") == "bamboo":
            option.click()

    available_pictures = [
        "images/bamboo/1_green_full.jpg", "images/bamboo/2_black_full.jpg",
        "images/bamboo/3_black_full.jpg", "images/bamboo/4_black_full.jpg",
        "images/bamboo/5_black_full.jpg", "images/bamboo/6_white_black_full.jpg",
        "images/bamboo/7_black_full.jpg", "images/bamboo/8_black_full.jpg",
        "images/bamboo/9_black_full.jpg", "images/bamboo/10_green_full.jpg",
        "images/bamboo/11_black_full.jpg", "images/bamboo/12_black_olive_full.jpg",
        "images/bamboo/13_gray_full.jpg", "images/bamboo/14_black_full.jpg",
        "images/bamboo/15_green_full.jpg", "images/bamboo/16_black_full.jpg",
        "images/bamboo/17_green_white_olive_full.jpg", "images/bamboo/18_black_full.jpg",
        "images/bamboo/19_green_full.jpg", "images/bamboo/20_gray_full.jpg",
        "images/bamboo/21_silver_full.jpg", "images/bamboo/22_white_full.jpg",
        "images/bamboo/23_black_olive_full.jpg", "images/bamboo/24_white_full.jpg",
        "images/bamboo/25_black_white_full.jpg"
    ]
    random_picture = random.choice(available_pictures)
    picture_input = browser.find_element_by_name("bg1_url")
    picture_input.send_keys(random_picture)

    save_button = browser.find_element_by_id("btnSave")
    save_button.click()

    # Wait until download started
    time.sleep(2)


def zip_files():
    print("📦  Creating zip archive ...")
    shutil.make_archive(DOWNLOADS_PATH + "/blog-images.zip", 'zip', DOWNLOADS_PATH + "/blog-images")
    shutil.rmtree(DOWNLOADS_PATH + "/blog-images")


if __name__ == "__main__":
    main()
