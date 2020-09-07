from selenium import webdriver

pyplanet_home_url = "https://pyplanet.herokuapp.com/"
pyplanet_app_url = pyplanet_home_url + "pyplanet/"

def find_pyplanet_link(driver):
    assert driver.find_elements_by_link_text("Login")
    assert driver.find_elements_by_link_text("Home")

    main = driver.find_element_by_tag_name("main")
    pyplanet_link = main.find_elements_by_link_text("PyPlanet Article Sharer App")[0]
    return pyplanet_link


def find_table(driver):
    tbl = driver.find_element_by_tag_name("table")

    th = tbl.find_element_by_tag_name("th")
    assert th.text == "Title"
    return tbl

def find_first_article_link(table):
    return table.find_element_by_xpath("/html/body/main/table/tbody/tr[1]/td/a")

def init_driver():
    return webdriver.Chrome()  # replaced Firefox by Chrome

def test_logged_out_view(driver):
    driver.get("https://pyplanet.herokuapp.com/")
    assert "PyBites 100 Days of Django" in driver.title

    pyplanet_link = find_pyplanet_link(driver)

    pyplanet_link.click()

    tbl = find_table(driver)
    assert len(tbl.find_elements_by_tag_name("tr")) - 1 == 100

    first_article_link = find_first_article_link(tbl)

    first_article_name = first_article_link.text
    first_article_url = first_article_link.get_attribute("href")
    first_article_link.click()
    main_div = driver.find_element_by_tag_name("main")
    article_header = main_div.find_element_by_tag_name("h2")
    assert first_article_name == article_header.text

    go_back = driver.find_elements_by_link_text("Go back")[0]
    homepage_link = go_back.get_attribute("href")
    assert homepage_link == pyplanet_app_url

    return first_article_url



def test_logged_in_view(driver, first_article_url):
    login_link = driver.find_elements_by_link_text("Login")[0]
    login_link.click()

    login_form = driver.find_element_by_tag_name("form")
    id_username = login_form.find_element_by_id('id_username')
    id_password = login_form.find_element_by_id('id_password')
    submit = login_form.find_element_by_class_name("pure-button")

    id_username.send_keys("guest")
    id_password.send_keys("changeme")
    submit.click()
    assert driver.current_url == pyplanet_home_url

    assert driver.find_element_by_link_text("Logout")
    assert driver.find_element_by_link_text("Home")
    login_div = driver.find_element_by_id("login")
    assert "Welcome back, guest!" in login_div.text

    validate_tweet_this(driver, first_article_url)

def validate_tweet_this(driver, article_url):
    driver.get(article_url)
    assert driver.find_element_by_link_text("Tweet this")


def validate_no_logged_out_tweets_for_you(driver, article_url):
    driver.get(article_url)
    # This doesn't work. Apparently the correct way is find_elements_by() - Gotta figure that out. Maybe. Someday :)
    assert not driver.find_element_by_link_text("Tweet this")


def validate_all_quiet_after_logout(driver):
    logout_link = driver.find_element_by_link_text("Logout")
    logout_link.click()
    header = driver.find_element_by_tag_name("h1")
    assert header.text == "See you!"

    para = driver.find_element_by_tag_name("p")
    assert para.text == "You have been successfully logged out."


if __name__ == "__main__":
    driver = init_driver()
    first_article_url = test_logged_out_view(driver)
    test_logged_in_view(driver, first_article_url)
    validate_all_quiet_after_logout(driver)
    # Attempt at a stretch goal. Not working :)
    # validate_no_logged_out_tweets_for_you(driver, first_article_url)

    driver.close()
    print("YAY! Test suite succeeded!")