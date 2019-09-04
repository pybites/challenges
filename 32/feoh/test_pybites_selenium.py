from selenium import webdriver

pyplanet_home_url = "https://pyplanet.herokuapp.com/"

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


def test_logged_out_view():
    driver = webdriver.Chrome()  # replaced Firefox by Chrome
    driver.get("https://pyplanet.herokuapp.com/")
    assert "PyBites 100 Days of Django" in driver.title

    pyplanet_link = find_pyplanet_link(driver)

    pyplanet_link.click()

    tbl = find_table(driver)

    assert len(tbl.find_elements_by_tag_name("tr")) - 1 == 100
    first_article_link = tbl.find_element_by_xpath("/html/body/main/table/tbody/tr[1]/td/a")
    article_name = first_article_link.text

    first_article_link.click()
    main_div = driver.find_element_by_tag_name("main")
    article_header = main_div.find_element_by_tag_name("h2")
    assert article_name == article_header.text

    go_back = driver.find_elements_by_link_text("Go back")[0]
    homepage_link = go_back.get_attribute("href")
    assert homepage_link == pyplanet_home_url + "pyplanet/"

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

    return driver

if __name__ == "__main__":
    driver = test_logged_out_view()

    driver.close()