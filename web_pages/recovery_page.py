import allure

from web_pages.base_page import BasePage
from web_locators.recovery_locators import RecoveryLocators as RL
from conftest import test_data
from data import Urls


class RecoveryPasswordPage(BasePage):

    @allure.step('Открытие страницы "Восстановление пароля"')
    def open_forgot_password_page(self):
        self.open_url(f'{Urls.MAIN_PAGE}{Urls.FORGOT_PASSWORD}')

    @allure.step('Получения заголовка')
    def check_title(self):
        return self.check_exist_element(RL.TITLE)

    @allure.step('Ввод данных в поле ввода "Email"')
    def input_email(self, test_data):
        self.set_text(RL.FILED_EMAIL, test_data['email'])

    @allure.step('Проверка наличия поля ввода "Пароль"')
    def check_exist_field_password(self):
        return self.check_exist_element(RL.FIELD_PASSWORD)

    @allure.step('Ввод данных в поле "Пароль"')
    def input_password(self, test_data):
        self.set_text(RL.FIELD_PASSWORD, test_data['password'])

    @allure.step('Получение статуса обводки поля ввода "Пароль"')
    def check_stroke_field_password(self):
        if self.find_element_visibility(RL.FIELD_ACTIVE_PASSWORD):
            return True

    @allure.step('Получение статуса поля ввода "Пароль"')
    def check_activ_fild_password(self):
        if self.find_element_visibility(RL.FIELD_ACTIVE_PASSWORD):
            return True

    @allure.step('Предусловие для кнопки "Показать/скрыть"')
    def precondition_for_button_show_hide(self,test_data):
        self.open_forgot_password_page()
        self.input_email(test_data)
        self.click_element_if_clickable(RL.BUTTON_RECOVERY)
