import selenium
from selenium import webdriver
import time

# Driver must be in home directory for this script to function
driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://pyplanet.herokuapp.com/')
driver.find_element_by_link_text('PyPlanet Article Sharer App').click()


def get_table_and_article():
    table_rows = driver.find_elements_by_tag_name('tr')
    test_article = table_rows[1].find_element_by_xpath(".//a")
    test_article_href = test_article.get_attribute('href')
    time.sleep(1)
    test_article.click()
    time.sleep(1)
    
    return test_article, test_article_href

assert "Title" in driver.find_element_by_tag_name('th').text
assert len(driver.find_elements_by_tag_name('tr')) == 101

test_article, test_article_href = get_table_and_article()

assert len(driver.find_elements_by_class_name('pure-button')) == 1
test_article_url = driver.current_url
assert test_article_href == test_article_url

driver.find_element_by_link_text('Login').click()
time.sleep(1)

driver.find_element_by_id('id_username').send_keys('guest')
driver.find_element_by_id('id_password').send_keys('changeme')
driver.find_element_by_tag_name('button').click()
time.sleep(1)

assert 'Welcome back' in driver.find_element_by_id('login').text
assert 'Logout' in driver.find_element_by_id('login').text
assert 'Home' in driver.find_element_by_id('login').text
driver.find_element_by_link_text('PyPlanet Article Sharer App').click()
driver.get(test_article_href)

driver.find_element_by_link_text('Logout').click()
assert 'logout' in driver.current_url
assert driver.find_element_by_tag_name('h1').text == "See you!"
assert driver.find_element_by_tag_name('p').text == "You have been successfully logged out."
assert driver.find_element_by_id('login').text == 'Login  | Home'

driver.close()
