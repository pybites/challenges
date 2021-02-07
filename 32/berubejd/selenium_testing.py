#!/usr/bin/env python3.8

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


ARTICLE_COUNT = 100


def click(driver, element):
    """ Function to replace native click() with JS implementation 
        This appears to be a bug in Selenium: https://github.com/SeleniumHQ/selenium/issues/4075 """

    driver.execute_script("arguments[0].click();", element)


def setup(url=None):
    if not url:
        url = "http://pyplanet.herokuapp.com/"

    print("\tStarting browser setup...")

    # This should work on both Windows and Linux
    # (and with a Windows chromedriver on an Ubuntu filesystem using WSL)
    # Returns first file in the current working directory called "chromedriver*"
    chrome_driver = None

    for file in Path.cwd().glob("chromedriver*"):
        if file.is_file():
            chrome_driver = file
            break

    if not chrome_driver:
        raise FileNotFoundError(
            "The chromedriver is not found in the current directory"
        )

    driver = webdriver.Chrome(executable_path=chrome_driver)
    driver.get(url)

    return driver


def test_homepage(driver):
    """ Test homepage header and nav links """

    print("\tPerforming anonymous user homepage testing...")

    # Header
    header = driver.find_element_by_xpath("/html/body/header/h1")
    assert (
        "PyBites 100 Days of Django" in header.text
    ), "Incorrect header text or text missing"

    # Login link
    login_link = driver.find_element_by_xpath('//*[@id="login"]/a[1]')
    assert "Login" in login_link.text, "Incorrect login link or link missing"

    # Home link
    home_link = driver.find_element_by_xpath('//*[@id="login"]/a[2]')
    assert "Home" in home_link.text, "Incorrect home link or link missing"


def test_sharer_app(driver):
    """ Test sharer app link and generated table """

    print("\tPerforming anonymous user App testing...")

    # Navigate to the Sharer App
    app_link = driver.find_element_by_xpath("/html/body/main/ul/li/a")
    click(driver, app_link)

    # Collect table header and links
    table_header = driver.find_element_by_xpath("/html/body/main/table/thead")
    assert "Title" in table_header.text, "Incorrect table header"

    table_links = driver.find_elements_by_xpath("/html/body/main/table/tbody/tr/td/a")
    assert len(table_links) == ARTICLE_COUNT, "Incorrect number of table rows"


def test_article_link(driver):
    """ Test table link links to proper article and the "Go back" button is the only one available 
        and works as expected (in next step) """

    print("\tPerforming anonymous user article testing...")

    # Find and save the first article in the table
    table_link = driver.find_element_by_xpath("/html/body/main/table/tbody/tr[1]/td/a")
    link_title = table_link.text

    # Navigate to that article
    click(driver, table_link)

    # Check that this is the correct article by comparing titles
    article_title = driver.find_element_by_xpath("/html/body/main/h2/a").text
    assert link_title == article_title, "Article detail doesn't match table link"

    # Collect list of buttons
    nav_buttons = driver.find_elements_by_xpath("/html/body/main/div/a")
    assert len(nav_buttons) == 1
    assert "Go back" in nav_buttons[0].text, "Incorrect 'Go back' link or link missing"
    assert "/pyplanet/" in nav_buttons[0].get_attribute(
        "href"
    ), "Incorrect link for 'Go back' button"

    # Return to previous page
    click(driver, nav_buttons[0])

    # Verify the first table entry one more time
    table_link = driver.find_element_by_xpath("/html/body/main/table/tbody/tr[1]/td/a")
    assert (
        link_title == table_link.text
    ), "Article list differs after returning from detail"


def test_login(driver, username=None, password=None):
    """ Log in to site with guest credentials """
    if not username:
        username = "guest"

    if not password:
        password = "changeme"

    print("\tPerforming guest user login testing...")

    # Find and click the login link
    login_link = driver.find_element_by_xpath('//*[@id="login"]/a[1]')
    click(driver, login_link)

    # Enter login credentials
    user_input = driver.find_element_by_name("username")
    driver.execute_script(f"arguments[0].value='{username}';", user_input)

    password_input = driver.find_element_by_name("password")
    driver.execute_script(f"arguments[0].value='{password}';", password_input)

    login_button = driver.find_element_by_css_selector("button")
    click(driver, login_button)

    # Verify we are back at the home page but logged in
    assert (
        "Welcome back, guest!" in driver.page_source
    ), "Greeting missing or login failed"

    # Logout link
    logout_link = driver.find_element_by_xpath('//*[@id="login"]/a[1]')
    assert "Logout" in logout_link.text, "Incorrect logout link or link missing"

    # Home link
    home_link = driver.find_element_by_xpath('//*[@id="login"]/a[2]')
    assert "Home" in home_link.text, "Incorrect home link or link missing"


def test_user_article_buttons(driver):
    """ Test logged in users have addition article button """

    print("\tPerforming guest user article testing...")

    # Navigate to the Sharer App
    app_link = driver.find_element_by_xpath("/html/body/main/ul/li/a")
    click(driver, app_link)

    # Find and save the first article in the table
    table_link = driver.find_element_by_xpath("/html/body/main/table/tbody/tr[1]/td/a")
    link_title = table_link.text

    # Navigate to that article
    click(driver, table_link)

    # Check that this is the correct article by comparing titles
    article_title = driver.find_element_by_xpath("/html/body/main/h2/a").text
    assert link_title == article_title, "Article detail doesn't match table link"

    # Collect list of buttons
    nav_buttons = driver.find_elements_by_xpath("/html/body/main/div/a")
    assert len(nav_buttons) == 2
    assert (
        "Tweet this" in nav_buttons[0].text
    ), "Incorrect 'Tweet this' link or link missing"
    assert "Go back" in nav_buttons[1].text, "Incorrect 'Go back' link or link missing"


def test_logout(driver):
    """ Test user logout """

    print("\tPerforming guest user logout testing...")

    # Find and click the Logout button
    logout_link = driver.find_element_by_xpath('//*[@id="login"]/a[1]')
    click(driver, logout_link)

    # Header
    header = driver.find_element_by_xpath("/html/body/header/h1")
    assert "See you!" in header.text, "Incorrect header text or text missing"

    # Login link
    login_link = driver.find_element_by_xpath('//*[@id="login"]/a[1]')
    assert "Login" in login_link.text, "Incorrect login link or link missing"

    # Home link
    home_link = driver.find_element_by_xpath('//*[@id="login"]/a[2]')
    assert "Home" in home_link.text, "Incorrect home link or link missing"

    # Proper body content and url
    assert (
        "You have been successfully logged out." in driver.page_source
    ), "Incorrect body text for logged out user or logout failed"
    assert (
        "logout" in driver.current_url
    ), "Incorrect URL for logged out user or logout failed"


if __name__ == "__main__":
    try:
        # Guest tests
        print("Begin anonymouse user testing.")

        driver = setup()
        test_homepage(driver)
        test_sharer_app(driver)
        test_article_link(driver)
        driver.close()

        print("Completed anonymouse user testing successfully!\n")

        # Logged in tests
        print("Begin guest user testing.")

        driver = setup()
        test_login(driver)
        test_user_article_buttons(driver)
        test_logout(driver)
        driver.close()

        print("Completed guest user testing successfully!\n")

    except Exception as e:
        print(f"\nThere was a failure during the test run:")
        print()
        print(f"\t{e}")
        print()

        # driver.close()
