import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_elements(driver: object, xpath: object, max_seconds_to_wait: object = 5,
                      number_of_expected_elements: object = 1) -> object:
    """Checking every second if list of elements under specified xpath was found
             :param driver: webdriver instance
             :param xpath: xpath of web element
             :return: list of found elements
             :param max_seconds_to_wait: maximum time in seconds to wait for element (default: 5)
             :param number_of_expected_elements: specifies minimum number of  elements to be found (default: 1)
          """

    for seconds in range(max_seconds_to_wait):
        elements = driver.find_elements_by_xpath(xpath)

        print(f'Total waiting {seconds} s')

        if len(elements) > number_of_expected_elements:
            return elements

        if seconds == (max_seconds_to_wait - 1):
            print('End of wait')
            assert len(elements) > number_of_expected_elements, \
                f'Expected {number_of_expected_elements} elements but found {len(elements)}' \
                    f' for xpath {xpath} in time of {max_seconds_to_wait}s'
        time.sleep(1)


def visibility_of_element_wait(driver, xpath, timeout=1):
    """Checking if element specified by xpath is visible on page
                 :param driver: webdriver instance
                 :param xpath: xpath of web element
                 :param timeout: time after looking for element will be stopped (default: 10)
                 :return: first element in list of found elements
              """
    text_message = f"Element for xpath: '{xpath}' and url: {driver.current_url} not found in {timeout} seconds"
    locator = (By.XPATH, xpath)
    element_located = EC.visibility_of_element_located(locator)
    # wait = WebDriverWait(driver, timeout)
    wait = WebDriverWait(driver.wrapped_driver, timeout)  # using pure driver
    element = wait.until(element_located, text_message)
    return element

