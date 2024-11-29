import allure
from web_pages.base_page import BasePage
from web_locators.recovery_locators import RecoveryLocators as RL
from data import Urls
from helper import move_to_element_and_click

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

    @allure.step('Нажатие на кнопку "Восстановить"')
    def click_recovery_button(self):
        self.click_element_if_clickable(RL.BUTTON_RECOVERY)

    @allure.step('Ввод данных в поле "Пароль"')
    def input_password(self, test_data):
        self.set_text(RL.FIELD_PASSWORD, test_data['password'])

    @allure.step('Нажатие на кнопку "Показать/скрыть"')
    def click_show_hide_button(self):
        move_to_element_and_click(self.driver, RL.BUTTON_SHOW_HIDE)

    @allure.step('Получение статуса обводки поля ввода "Пароль"')
    def check_stroke_field_password(self):
        return self.check_exist_element(RL.FIELD_ACTIVE_PASSWORD)

    @allure.step('Получение статуса поля ввода "Пароль"')
    def check_activ_fild_password(self):
        return self.check_exist_element(RL.FIELD_ACTIVE_PASSWORD)

    @allure.step('Предусловие для кнопки "Показать/скрыть"')
    def precondition_for_button_show_hide(self, test_data):
        self.open_forgot_password_page()
        self.input_email(test_data)
        self.click_recovery_button()
