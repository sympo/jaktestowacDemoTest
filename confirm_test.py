import time
import unittest

from helpers import operational_helpers as oh
from selenium import webdriver

from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.screenshotlistener import ScreenshotListener
from helpers.wrappers import screenshot_decorator


class LostHatShoppingCartTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.art_product_url = self.base_url + '9-art'
        driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())
        self.ef_driver.maximize_window()
        # self.driver.implicitly_wait(10)
        time.sleep(2)

    @classmethod
    def tearDown(self):
         self.ef_driver.quit()

    @screenshot_decorator
    def test_adding_item_to_shopping_cart(self):
        product_xpath = '//*[@id="js-product-list"]/div[1]/article[3]/div/a/img'
        add_button_xpath = '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button'
        expected_text = '\ue876Product successfully added to your shopping cart'
        # confirmation_modal_title_xpath = '//*[@id="lol_nie_ma"]'
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'

        driver = self.ef_driver
        time.sleep(2)
        driver.get(self.art_product_url)
        time.sleep(2)

        product_element = driver.find_element_by_xpath(product_xpath)
        product_element.click()
        time.sleep(2)

        add_button_element = driver.find_element_by_xpath(add_button_xpath)
        add_button_element.click()
        # confirmation_modal_element = WebDriverWait(driver, 10).until(
        #   EC.visibility_of_element_located((By.XPATH, confirmation_modal_title_xpath)),
        #   f"Element for xpath: '{confirmation_modal_title_xpath}' and url: {driver.current_url} not found")

        confirmation_modal_element = oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath, 1)
        self.assertEqual(expected_text, confirmation_modal_element.text)

