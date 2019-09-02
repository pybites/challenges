from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # replaced Firefox by Chrome
driver.get("https://pyplanet.herokuapp.com")
#assert "Python" in driver.title
assert "PyBites 100 Days of Django" in driver.title

assert driver.find_elements_by_link_text("Login")
assert driver.find_elements_by_link_text("Home")

assert driver.find_element_by_tag_name("main")
assert driver.find_elements_by_link_text("PyPlanet Article Sharer App")

driver.close()