import unittest
from selenium import webdriver

BASE_URL = 'http://pyplanet.herokuapp.com/'
PAGE_TITLE = 'PyBites 100 Days of Django'
APP_URL = 'http://pyplanet.herokuapp.com/pyplanet/'
APP_NAME = 'PyPlanet Article Sharer App'
USERNAME, PASSWORD = 'guest', 'changeme'
TABLE_CLASS = 'pure-table'  # TODO: use html id/name


class TestPyBitesPyplanet(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def _get_first_article_title(self, driver):
        table = driver.find_element_by_xpath(
            "//table[@class='{}']".format(TABLE_CLASS))
        return table.find_elements_by_xpath(".//td")[0].text

    def test_logged_out_views(self):
        driver = self.driver
        driver.get(BASE_URL)

        self.assertEqual(PAGE_TITLE, driver.title)
        h1_text = driver.find_element_by_tag_name('h1').text
        self.assertEqual(PAGE_TITLE, h1_text)

        first_app_link_name = driver.find_element_by_xpath(
            "//main/ul/li[1]/a").text
        self.assertEqual(APP_NAME, first_app_link_name)

        driver.find_element_by_link_text(APP_NAME).click()
        self.assertEqual(self.driver.current_url, APP_URL)

        self.assertIn('<th>Title</th>', driver.page_source)
        self.assertEqual(driver.page_source.count('<td'), 100)

        first_article = self._get_first_article_title(driver)
        driver.find_element_by_link_text(first_article).click()

        title_article_page = driver.find_element_by_tag_name('h2').text
        self.assertEqual(title_article_page, first_article)
        self.assertIn('Article:', driver.page_source)
        self.assertIn('(published: ', driver.page_source)

        self.assertIn('Go back', driver.page_source)
        go_back_btn = driver.find_element_by_link_text('Go back')
        go_back_link = go_back_btn.get_attribute('href')
        self.assertEqual(go_back_link, APP_URL)
        self.assertNotIn('Tweet this', driver.page_source)

    def test_login_logout_process_and_views(self):
        driver = self.driver
        driver.get(APP_URL)

        self.assertIn('<a href="/">Home</a>', driver.page_source)
        self.assertIn('<a href="/login/">Login</a>', driver.page_source)
        self.assertNotIn('<a href="/logout/">Logout</a>', driver.page_source)

        driver.find_element_by_link_text('Login').click()

        username_field = driver.find_element_by_name('username')
        username_field.send_keys(USERNAME)
        password_field = driver.find_element_by_name('password')
        password_field.send_keys(PASSWORD)

        # TODO: need html id/name on button
        btn_xpath = "//button[contains(@class, 'pure-button-primary')]"
        login_btn = driver.find_element_by_xpath(btn_xpath)
        login_btn.click()

        # TODO: when logging in, need to redirect to previous page
        driver.get(APP_URL)

        self.assertNotIn('<a href="/login/">Login</a>', driver.page_source)
        self.assertIn('Welcome back, guest', driver.page_source)
        self.assertIn('<a href="/logout/">Logout</a>', driver.page_source)

        first_article = self._get_first_article_title(driver)
        driver.find_element_by_link_text(first_article).click()

        self.assertIn('Go back', driver.page_source)
        self.assertIn('Tweet this', driver.page_source)
        tweet_btn = driver.find_element_by_link_text('Tweet this')
        tweet_link_text = tweet_btn.get_attribute('href')
        regex = r'^https://twitter.com/intent/tweet\?text=.*via=pybites$'
        self.assertRegex(tweet_link_text, regex)

        driver.find_element_by_link_text('Logout').click()
        self.assertIn('logout', self.driver.current_url)
        self.assertIn('See you!', driver.page_source)
        self.assertIn('successfully logged out.', driver.page_source)
        self.assertIn('<a href="/">Home</a>', driver.page_source)
        self.assertIn('<a href="/login/">Login</a>', driver.page_source)
        self.assertNotIn('<a href="/logout/">Logout</a>', driver.page_source)
