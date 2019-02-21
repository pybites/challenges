import re

import pytest
from selenium import webdriver


BASE_URL = 'http://pyplanet.herokuapp.com/'
PAGE_TITLE = 'PyBites 100 Days of Django'
APP_URL = 'http://pyplanet.herokuapp.com/pyplanet/'
APP_NAME = 'PyPlanet Article Sharer App'
USERNAME, PASSWORD = 'guest', 'changeme'
TABLE_CLASS = 'pure-table'


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def get_first_article_title(driver):
    table = driver.find_element_by_xpath(f'//table[@class="{TABLE_CLASS}"]')
    return table.find_elements_by_xpath(".//td")[0].text


def test_login_logout_process_and_views(driver):
    driver.get(APP_URL)

    assert '<a href="/">Home</a>' in driver.page_source
    assert '<a href="/login/">Login</a>' in driver.page_source
    assert '<a href="/logout/">Logout</a>' not in driver.page_source

    driver.find_element_by_link_text('Login').click()
    username_field = driver.find_element_by_name('username')
    username_field.send_keys(USERNAME)
    password_field = driver.find_element_by_name('password')
    password_field.send_keys(PASSWORD)

    btn_xpath = "//button[contains(@class, 'pure-button-primary')]"
    login_btn = driver.find_element_by_xpath(btn_xpath)
    login_btn.click()

    driver.get(APP_URL)

    assert '<a href="/login/">Login</a>' not in driver.page_source
    assert 'Welcome back, guest' in driver.page_source
    assert '<a href="/logout/">Logout</a>' in driver.page_source

    first_article = get_first_article_title(driver)
    driver.find_element_by_link_text(first_article).click()

    assert 'Go back' in driver.page_source
    assert 'Tweet this' in driver.page_source
    tweet_btn = driver.find_element_by_link_text('Tweet this')
    tweet_link_text = tweet_btn.get_attribute('href')
    regex = r'^https://twitter.com/intent/tweet\?text=.*via=pybites$'
    assert re.match(regex, tweet_link_text)

    driver.find_element_by_link_text('Logout').click()
    assert 'logout' in driver.current_url
    assert 'See you!' in driver.page_source
    assert 'successfully logged out.' in driver.page_source
    assert '<a href="/">Home</a>' in driver.page_source
    assert '<a href="/login/">Login</a>' in driver.page_source
    assert '<a href="/logout/">Logout</a>' not in driver.page_source


def test_homepage_view(driver):
    driver.get(BASE_URL)

    assert PAGE_TITLE == driver.title
    h1_text = driver.find_element_by_tag_name('h1').text
    assert PAGE_TITLE == h1_text

    first_app_link_name = driver.find_element_by_xpath(
        '//main/ul/li[1]/a').text
    assert APP_NAME == first_app_link_name


def test_article_list_view(driver):
    driver.get(BASE_URL)

    driver.find_element_by_link_text(APP_NAME).click()
    assert driver.current_url == APP_URL

    assert '<th>Title</th>' in driver.page_source
    assert driver.page_source.count('<td') == 100


def test_single_article_view(driver):
    driver.get(BASE_URL)

    driver.find_element_by_link_text(APP_NAME).click()
    first_article = get_first_article_title(driver)
    driver.find_element_by_link_text(first_article).click()

    title_article_page = driver.find_element_by_tag_name('h2').text
    assert title_article_page == first_article
    assert 'Article:' in driver.page_source
    assert '(published: ' in driver.page_source

    assert 'Go back' in driver.page_source
    go_back_btn = driver.find_element_by_link_text('Go back')
    go_back_link = go_back_btn.get_attribute('href')
    assert go_back_link == APP_URL
    assert 'Tweet this' not in driver.page_source
