import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LostHatSearchTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
        self.driver.maximize_window()
        time.sleep(2)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_sanity_search_on_main_page(self):
        search_phase = 'HUMMINGBIRD'
        expected_element_name = 'Hummingbird Printed Sweater'
        xpath = '//*[@name="s"] '
        result_xpath = '//*[@class="product-miniature js-product-miniature"]'

        driver = self.driver
        driver.get(self.base_url)
        search_input_element = self.driver.find_element_by_xpath(xpath)
        search_input_element.send_keys(search_phase)
        time.sleep(2)
        search_input_element.send_keys(Keys.ENTER)
        time.sleep(2)

        result_elements = self.driver.find_elements_by_xpath(result_xpath)
        found_elements_number = 0
        for element in result_elements:
            if expected_element_name in element.text:
                found_elements_number = found_elements_number + 1

        self.assertEqual(1, found_elements_number, f"We expect 1 and actaal number of found items is {found_elements_number}")






