import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls
from web_pages.base_page import BasePage
from web_locators.profile_locators import ProfileLocators as PL
from web_locators.login_locators import LoginLocators as LL

class ProfilePage(BasePage):

    @allure.step('Проверка наличия элементов на открытой странице')
    def check_open_page(self):
        self.find_element_visibility(PL.BUTTON_PROFILE)
        return self.check_exist_element(PL.BUTTON_PROFILE)

    @allure.step('Нажатие на кнопку "История заказов" с проверкой открытия')
    def open_history_page(self):
        self.find_element_visibility(PL.BUTTON_HISTORY)
        self.click_element_if_clickable(PL.BUTTON_HISTORY)
        if self.get_url() == Urls.MAIN_PAGE + Urls.HISTORY_PAGE:
            return True
        else:
            return False

    @allure.step("Проверка нахождения идентификатора заказа в истории")
    def found_order_at_history(self, order_id, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: any(
                    order_id in element.text for element in self.find_until_all_elements_located(PL.ORDERS_AT_HISTORY))
            )
            return True
        except TimeoutException:
            return False

    @allure.step('Нажатие кнопки "Выход" с проверкой выхода')
    def exit(self):
        self.click_element_if_clickable(PL.BUTTON_EXIT)
        self.find_element_not_visibility(PL.BUTTON_EXIT)
        if self.get_url() == Urls.MAIN_PAGE + Urls.LOGIN:
            return True
        else:
            return False

    @allure.step('Авторизация')
    def authorization(self, test_data):
        name = test_data['name']
        password = test_data['password']
        email = test_data['email']

        self.open_url(Urls.MAIN_PAGE + Urls.REGISTER)
        self.find_element_visibility(LL.FIELD_NAME_FOR_REG)

        self.set_text(LL.FIELD_NAME_FOR_REG, name)
        self.set_text(LL.FIELD_EMAIL_FOR_REG, email)
        self.set_text(LL.FIELD_PASSWORD_FOR_REG, password)

        self.click_element_if_clickable(LL.BUTTON_FOR_REG)
        self.find_element_not_visibility(LL.BUTTON_FOR_REG)

        self.find_element_visibility(LL.FIELD_EMAIL_FOR_LOGIN)
        self.set_text(LL.FIELD_EMAIL_FOR_LOGIN, email)
        self.set_text(LL.FIELD_PASSWORD_FOR_LOGIN, password)

        self.click_element_if_clickable(LL.BUTTON_FOR_LOGIN)
        self.find_element_not_visibility(LL.BUTTON_FOR_LOGIN)

    def precondition_for_tests(self, test_data):
        self.authorization(test_data)
        self.click_profile_page_button()

    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def click_profile_page_button(self):
        self.click_element_if_clickable(PL.BUTTON_PROFILE_PAGE)
