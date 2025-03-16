from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://pyplanet.herokuapp.com/")

print(f"Confirming the title of the driver: {driver.title}")
assert "PyBites 100 Days of Django" == driver.title

""" Going to next page by clicking the link """
driver.find_element_by_xpath('//main/ul/li[1]/a').click()

""" Confirm title of the table """
print("Confirming the title of the table now.")
assert driver.find_element_by_xpath('//main/table/thead/tr/th').text == "Title"

""" Grab the table body to go through rows to confirm there's 100 """
tbl = driver.find_element_by_xpath('//main/table/tbody')
total_rows = tbl.find_elements_by_tag_name("tr")
print(f"Number of rows in the table is: {len(total_rows)}")

elem = driver.find_element_by_xpath('//main/table/tbody/tr[1]/td/a')
elem_text = elem.text
print(f"About to click on '{elem_text}'.")
elem.click()

""" Checks the blog title matches and you aren't logged in. """
go_back = driver.find_element_by_xpath('//main/div/a')

print(f"Confirming the go back buttons says that: {go_back.text}.")
assert go_back.text == "Go back"

""" TODO Confirm only go back and not other logged in functionality."""

header = driver.find_element_by_xpath('//main/h2/a').text

print(f"Confirming header matches: {header}.")
assert header == elem_text
go_back.click()

""" At table and about to log in """

log_in = driver.find_element_by_link_text('Login').click()
driver.find_element_by_id('id_username').send_keys('guest')
driver.find_element_by_id('id_password').send_keys('changeme')
driver.find_element_by_class_name('pure-button-primary').click()

"""" Confirm logged in and at home page """
print("Confirming we're logged in and at the homepage again.")
assert driver.find_element_by_xpath('//header/h1').text == driver.title
assert driver.find_element_by_xpath('//header/div').text == "Welcome back, guest! Logout  | Home"
elems = driver.find_elements_by_xpath('//header/div/a')
assert elems[0].text == "Logout"
assert elems[1].text == "Home"

driver.find_element_by_xpath('//main/ul/li[1]/a').click()
elem = driver.find_element_by_xpath('//main/table/tbody/tr[1]/td/a')
print(f"About to click on '{elem.text}'.")
elem.click()

assert driver.find_element_by_xpath('//main/div').text == "Tweet this Go back"

driver.find_element_by_xpath('//header/div/a').click()
print(f"About to confirm {driver.find_element_by_xpath('//header/h1').text} and {driver.find_element_by_xpath('//main/p').text}")
assert driver.find_element_by_xpath('//header/h1').text == "See you!"
assert driver.find_element_by_xpath('//main/p').text == "You have been successfully logged out."

print("Congratulations! You passed all the tests.")
driver.close()

