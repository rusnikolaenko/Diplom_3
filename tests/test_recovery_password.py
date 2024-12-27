import allure
from web_pages.login_page import LoginPage
from web_pages.recovery_page import RecoveryPasswordPage

class TestRecoveryPassword:

    @allure.title('Проверка открытия страницы "Восстановление пароля"')
    def test_open_recovery_page(self, driver):
        lp = LoginPage(driver)
        lp.open_login_page()
        lp.click_recovery_password_button()

        rp = RecoveryPasswordPage(driver)
        assert rp.check_title() is True, 'Страница восстановления пароля не открыта'

    @allure.title('Проверка ввода почты и нажатие на кнопку "Восстановить"')
    def test_input_data_and_click_button(self, driver, test_data):
        rpp = RecoveryPasswordPage(driver)
        rpp.open_forgot_password_page()
        rpp.input_email(test_data)
        rpp.click_recovery_button()
        assert rpp.check_exist_field_password() is True, ('После нажатия на кнопку "Восстановить" '
                                                          'не открылась страница смены пароля')

    @allure.step('Проверка статуса поля ввода "Пароль" после нажатия кнопки "Показать/скрыть"')
    def test_button_show_hide(self, driver, test_data):
        rpp = RecoveryPasswordPage(driver)
        rpp.precondition_for_button_show_hide(test_data)
        rpp.input_password(test_data)
        rpp.click_show_hide_button()
        assert (rpp.check_stroke_field_password()
                is True and rpp.check_activ_fild_password() is True), ('Статус поля ввода "Пароль" '
                                                                       'не соответствует ожидаемому"')
