import time
import unittest
from selenium import webdriver

from helpers import functional_helpers as fh

from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from helpers.screenshotlistener import ScreenshotListener
from helpers.wrappers import screenshot_decorator


class LostHatLoginPageTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())
        self.ef_driver.maximize_window()
        time.sleep(2)

    @classmethod
    def tearDown(self):
        self.ef_driver.quit()

    def assert_element_text(self, driver, xpath, expected_text):
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Expected text differ from actual on page: {driver.current_url}')

    @screenshot_decorator
    def test_login_text_header(self):
        expected_text = 'Log in to your account'   #oczekiwany tekst
        xpath = '//header[@class="page-header"]'

        driver = self.ef_driver
        time.sleep(2)
        driver.get(self.login_url)
        time.sleep(2)

        self.assert_element_text(driver, xpath, expected_text)

    @screenshot_decorator
    def test_correct_login(self):
        # expected_text is a user name and user surname used during registration
        expected_text = 'm s'
        user_email = 'sympo600074@wp.pl'
        user_pass = 'status123'
        username_xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'

        driver = self.ef_driver
        driver.get(self.login_url)
        time.sleep(2)

        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, username_xpath, expected_text)

    @screenshot_decorator
    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        user_email = 'asdasd@wp.pl'
        user_pass = 'asdas1221'
        alert_xpath = '//*[@id="content"]/section/div/ul/li'

        driver = self.ef_driver
        driver.get(self.login_url)
        time.sleep(2)

        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, alert_xpath, expected_text)
