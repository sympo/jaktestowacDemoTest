import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.screenshotlistener import ScreenshotListener
from helpers.wrappers import screenshot_decorator


class LostHatSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.clothes_url = self.base_url + '3-clothes'
        self.accessories_url = self.base_url + '6-accessories'
        self.art_product_url = self.base_url + '9-art'
        driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())
        self.ef_driver.maximize_window()
        time.sleep(2)

    @classmethod
    def tearDownClass(self):
        self.ef_driver.quit()

    def get_page_title(self, url):
        self.ef_driver.get(url)
        return self.ef_driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title,
                         f'Expected: {expected_title} differ from actual title {actual_title} on page: {url}')

    @screenshot_decorator
    def test_base_page(self):
        expected_title = 'Lost Hat'
        self.assert_title(self.base_url, expected_title)
        time.sleep(2)

    @screenshot_decorator
    def test_login_page(self):
        expected_title = 'Login'
        self.assert_title(self.login_url, expected_title)
        time.sleep(2)

    @screenshot_decorator
    def test_clothes_page(self):
        expected_title = 'Clothes'
        self.assert_title(self.clothes_url, expected_title)
        time.sleep(2)

    @screenshot_decorator
    def test_accessories_page(self):
        expected_title = 'Accessories'
        self.assert_title(self.accessories_url, expected_title)
        time.sleep(2)

    @screenshot_decorator
    def test_art_page(self):
        expected_title = 'Art'
        self.assert_title(self.art_product_url, expected_title)

    @screenshot_decorator
    def test_search(self):
        xpath = '//*[@name="s"] '
        # xpath_search = '//*[@id="search_widget"]/form/button/i'
        search_text = 'mug'
        minimun_elements = 5
        result_xpath = '//*[@class="product-miniature js-product-miniature"]'

        driver = self.ef_driver
        driver.get(self.base_url)
        search_input_element = self.ef_driver.find_element_by_xpath(xpath)
        search_input_element.send_keys(search_text)
        search_input_element.send_keys(Keys.ENTER)

        results_elements = self.ef_driver.find_elements_by_xpath(result_xpath)
        self.assertLessEqual(minimun_elements, len(results_elements), f"Expected number {minimun_elements}"
        f" isn't less or equal than actual number of elements found: {len(results_elements)}")








