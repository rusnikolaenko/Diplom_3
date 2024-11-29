import allure
from web_pages.base_page import BasePage
from data import Urls
from web_locators.login_locators import LoginLocators

class LoginPage(BasePage):
    @allure.step('Открытие страницы "Вход"')
    def open_login_page(self):
        self.open_url(f'{Urls.MAIN_PAGE}{Urls.LOGIN}')

    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def click_recovery_password_button(self):
        self.click_element_if_clickable(LoginLocators.BUTTON_RECOVERY_PASSWORD)
