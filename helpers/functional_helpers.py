import time


def user_login(driver, user_email, user_pass):
    """
    :param driver: webdriver instance
    :param user_email: user email
    :param user_pass: user password
    :return None
    """
    # finding login input box and sending value
    login_input_element = driver.find_element_by_xpath('//*[@type="email"]')
    login_input_element.send_keys(user_email)
    time.sleep(2)

    # finding password input box and sending value
    login_input_element = driver.find_element_by_xpath('//*[@type="password"]')
    login_input_element.send_keys(user_pass)
    time.sleep(2)
    # finding button 'sign in'

    button_next_element = driver.find_element_by_xpath('//*[@id="submit-login"]')
    time.sleep(2)
    button_next_element.click()

    #finding search box and sending value

