import time
import unittest
from selenium import webdriver


class LostHatProductPageTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
        time.sleep(2)


    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_check_product_name(self):
        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        name_xpath = '//*[@class="col-md-6"]//*[@itemprop="name"]'

        driver = self.driver
        driver.get(self.sample_product_url)
        time.sleep(2)

        self.assert_element_text(driver, name_xpath, expected_product_name)

    def test_check_product_price(self):
        expected_product_price = 'PLN23.52'
        price_xpath = '//*[@class="current-price"]//*[@itemprop="price"]'

        driver = self.driver
        driver.get(self.sample_product_url)
        time.sleep(2)

        self.assert_element_text(driver, price_xpath, expected_product_price)

    def assert_element_text(self, driver, xpath, expected_text):
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text, f'Expected text differ from actual on page: {driver.current_url}')