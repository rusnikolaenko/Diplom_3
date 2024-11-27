import allure

from data import Urls
from web_pages.base_page import BasePage
from web_locators.profile_locators import ProfileLocators as PL
from web_locators.login_locators import LoginLocators as LL
from conftest import test_data


class ProfilePage(BasePage):

    @allure.step('Проверка наличия элементов на открытой странице')
    def check_open_page(self):
        self.find_element_visibility(PL.BUTTON_PROFILE)
        return self.check_exist_element(PL.BUTTON_PROFILE)

    @allure.step('Открытие страницы "История заказов" с проверкой открытия')
    def open_history_page(self):
        self.find_element_visibility(PL.BUTTON_HISTORY)
        button_history = self.find_element_visibility(PL.BUTTON_HISTORY)
        self.driver.execute_script('arguments[0].click();', button_history)
        if self.get_url() == Urls.MAIN_PAGE + Urls.HISTORY_PAGE:
            return True
        else:
            return False

    @allure.step("Проверка нахождение идентификатора заказа в истории")
    def found_order_at_history(self, order_id):
        elements = self.find_until_all_elements_located(PL.ORDERS_AT_HISTORY)

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step('Нажатие кнопки "Выход" с проверкой выхода')
    def exit(self):
        button_exit = self.find_element_visibility(PL.BUTTON_EXIT)
        self.driver.execute_script('arguments[0].click();', button_exit)
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
        self.click_element_if_clickable(PL.BUTTON_PROFILE_PAGE)
