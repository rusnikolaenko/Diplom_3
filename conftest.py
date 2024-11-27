import pytest

from selenium import webdriver
from data import Urls
from helper import helper_password, helper_name, helper_email


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')  # Включаем headless-режим
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        browser = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # Включаем headless-режим
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Chrome(options=options)

    browser.get(Urls.MAIN_PAGE)
    yield browser
    browser.quit()


@pytest.fixture
def test_data():
    data = {
        'password': helper_password(),
        'email': helper_email(),
        'name': helper_name()
    }

    return data
