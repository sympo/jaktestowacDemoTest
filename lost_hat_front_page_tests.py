import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from helpers.screenshotlistener import ScreenshotListener
from helpers.wrappers import screenshot_decorator


class LostHatFrontPageTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())
        self.ef_driver.maximize_window()
        time.sleep(2)

    @classmethod
    def tearDown(self):
        self.ef_driver.quit()

    @screenshot_decorator
    def test_slider(self):
        slider_xpath = ('//*[@id="carousel"]/ul/li[2]/a/figure/img')
        driver = self.ef_driver
        driver.get(self.base_url)
        time.sleep(2)
        driver.find_element_by_xpath(slider_xpath)

    @screenshot_decorator
    def test_slider_minimum_size(self):
        expected_min_height = 300
        expected_min_width = 600
        slider_xpath = '//*[@id="carousel"]'
        driver = self.ef_driver

        driver.get(self.base_url)
        slider_element = driver.find_element_by_xpath(slider_xpath)
        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']

        with self.subTest('Element height'):
            self.assertLess(expected_min_height, actual_slider_height,
                        f'Element height found by xpath {slider_xpath} on page {driver.current_url} '
                        f'is smaller than expected {expected_min_height}px')

        with self.subTest('Element width'):
            self.assertLess(expected_min_width, actual_slider_width,
                        f'Element width found by xpath {slider_xpath} on page {driver.current_url} '
                        f'is smaller than expected {expected_min_width}px')

    @screenshot_decorator
    def test_slider_contain_exact_number_of_slides(self):
        expected_number_of_slides = 3
        slides_xpath = '//*[@id="carousel"]/ul/li'
        driver = self.ef_driver
        driver.get(self.base_url)

        slider_elements = driver.find_elements_by_xpath(slides_xpath)
        actual_numer_of_slides = len(slider_elements)
        self.assertEqual(expected_number_of_slides, actual_numer_of_slides,
                         f'Slides number differ for page {self.base_url}')

    @screenshot_decorator
    def test_slides_required_title_text(self):
        expected_text_included_in_slide = 'sample'
        slides_titles_xpath = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'
        driver = self.ef_driver

        driver.get(self.base_url)
        title_elements = driver.find_elements_by_xpath(slides_titles_xpath)

        for title_element in title_elements:
            title_element_text = title_element.get_attribute("textContent")
            title_element_text_lower = title_element_text.lower()
            with self.subTest(title_element_text_lower):
                self.assertIn(expected_text_included_in_slide, title_element_text_lower,
                              f"Slides does not contain expected text for page {self.base_url}")
# product-miniature js-product-miniature

    @screenshot_decorator
    def test_number_of_product(self):
        expected_number_of_product = 8
        product_xpath = '//*[@class="product-miniature js-product-miniature"]'
        driver = self.ef_driver

        driver.get(self.base_url)
        product_elements = driver.find_elements_by_xpath(product_xpath)
        actual_number_of_product = len(product_elements)
        self.assertEqual(expected_number_of_product, actual_number_of_product,
                         f'Product number differ for page {self.base_url}')

    @screenshot_decorator
    def test_featured_product_price_in_pl(self):
        expected_product_currency = 'PLN'
        products_price_xpath = '//*[@class="product-miniature js-product-miniature"]//*[@class="[price"]'

        driver = self.ef_driver
        driver.get(self.base_url)

        product_price_elements = driver.find_elements_by_xpath(products_price_xpath)

        for product_price_element in product_price_elements:
            product_price_element_text = product_price_element.get_attribute("textContent")
            with self.subTest(product_price_element_text):
                self.assertIn(expected_product_currency,product_price_element_text,
                              f"Explected text not found in product description for page {self.base_url}")













