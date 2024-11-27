import random
import string

from selenium.webdriver import ActionChains


def move_to_element_and_click(driver, locator):
    element = driver.find_element(*locator)
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

def helper_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def helper_email():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + '@ya.ru'


def helper_name():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))