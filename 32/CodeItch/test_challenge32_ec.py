"""
32 - Test a Simple Django App With Selenium

Some of these tests could have been combined better, use of a class
But I preferred banging it out **and** having ONE ASSERT TEST per function.

EC was more necessary than expected, but also wonder if it was the differance
between headed and headless. Headless just worked better (a lot better. No focus issues)




"""

__author__ = "CodeItch@Pybites/CodeItchNY@Github"
__date__ ="December 1, 2019"



import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import  NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    options = Options()
    options.add_argument('disable-gpu')
    options.add_argument("headless")

    url = 'https://pyplanet.herokuapp.com/'

    # driver binary options all send errors? Later
    driver_binary = r"X:\IDrive-Sync\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_binary, options=options)
    driver.implicitly_wait(10)

    driver.get(url)
    yield driver
    driver.close()


def test_site_up(browser):
    assert "PyBites 100 Days of Django" == browser.title


def test_has_sharer_app_link(browser):
    assert browser.find_element_by_link_text('PyPlanet Article Sharer App')


def test_sharer_app_link_works(browser):
    browser.find_element_by_link_text('PyPlanet Article Sharer App').click()
    assert "pyplanet" in browser.current_url


def test_page_has_table(browser):
    browser.find_element_by_link_text('PyPlanet Article Sharer App').click()
    assert "Title" == browser.find_element_by_tag_name("th").text


def test_page_has_100_articles(browser):
    browser.find_element_by_link_text('PyPlanet Article Sharer App').click()
    tr_list = browser.find_elements_by_xpath("//tbody/tr")
    assert len(tr_list) == 100


def test_check_one_back_button(browser):
    wait = WebDriverWait(browser, 10)
    browser.find_element_by_link_text('PyPlanet Article Sharer App').click()
    elem = browser.find_element_by_css_selector("table.pure-table>tbody>tr>td>a")
    elem.click()
    buttons = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".pure-button")))
    assert len(buttons) == 1 and buttons[0].text.lower() == "Go back".lower()


def test_right_url_after_navigation(browser):
    wait = WebDriverWait(browser, 10)
    browser.find_element_by_link_text('PyPlanet Article Sharer App').click()
    elem = browser.find_element_by_css_selector("table.pure-table>tbody>tr>td>a")
    link_href = elem.get_attribute("href")
    elem.click()
    wait.until(EC.url_matches(link_href))
    assert link_href == browser.current_url


def test_verify_go_back_button(browser):
    wait = WebDriverWait(browser, 10)
    browser.find_element_by_link_text('PyPlanet Article Sharer App').click()
    article_home = browser.current_url
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"table.pure-table>tbody>tr>td>a"))).click()
    button_text = browser.find_element_by_css_selector(".pure-button").text.strip()
    browser.find_element_by_link_text(button_text).click()
    wait.until(EC.url_matches(article_home))
    assert browser.current_url == article_home


def test_check_bad_login(browser):
    # Bad password
    wait = WebDriverWait(browser, 3)
    browser.find_element_by_link_text('Login').click()
    # just wait on all input fields
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("guest")
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("wrongwrongwrong", Keys.RETURN)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li")))
    assert "Please enter a correct username and password" in browser.page_source

def test_check_good_login(browser):
    # Normally in env.
    # Hurts to write this like this.
    wait = WebDriverWait(browser, 3)
    browser.find_element_by_link_text('Login').click()
    # just wait on all input fields
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("guest")
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("changeme", Keys.RETURN)
    assert "Welcome back, guest!" in browser.page_source


def test_tweet_this_exists(browser):
    wait = WebDriverWait(browser, 3)
    browser.find_element_by_link_text('Login').click()
    # just wait on all input fields
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("guest")
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("changeme", Keys.RETURN)
    browser.find_element_by_link_text('PyPlanet Article Sharer App').click()  # Correct navigation?
    elem = browser.find_element_by_css_selector("table.pure-table>tbody>tr>td>a")
    elem.click()
    assert browser.find_element_by_link_text("Tweet this").text.strip() == "Tweet this"


def test_logout(browser):
    wait = WebDriverWait(browser, 3)
    browser.find_element_by_link_text('Login').click()
    # just wait on all input fields
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("guest")
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("changeme", Keys.RETURN)
    browser.find_element_by_link_text("Logout").click()
    assert "logout" in browser.current_url
    assert "See you!" == browser.find_element_by_css_selector("H1").text
    assert "You have been successfully logged out" in browser.find_element_by_css_selector("p").text
    assert ">Login<" in browser.page_source
    assert ">Home<" in browser.page_source




