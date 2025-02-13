import allure
from web_pages.profile_page import ProfilePage

class TestProfile:

    @allure.title('Открытие страницы "Личный кабинет"')
    def test_open_profile_page(self, driver, test_data):
        pp = ProfilePage(driver)
        pp.authorization(test_data)
        pp.click_profile_page_button()
        assert pp.check_open_page() is True

    @allure.title('Переход на страницу "История заказов"')
    def test_open_history(self, driver, test_data):
        pp = ProfilePage(driver)
        pp.precondition_for_tests(test_data)
        assert pp.open_history_page() is True

    @allure.title('Проверка выхода пользователя при нажатие на кнопку "Выйти"')
    def test_exit(self, driver, test_data):
        pp = ProfilePage(driver)
        pp.precondition_for_tests(test_data)
        assert pp.exit() is True
