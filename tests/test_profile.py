import allure
from web_pages.profile_page import ProfilePage
from web_locators.profile_locators import ProfileLocators as PL


class TestProfile:

    @allure.title('Открытие страницы "Личный кабинет"')
    def test_open_profile_page(self, driver, test_data):
        pp = ProfilePage(driver)
        pp.authorization(test_data)
        pp.click_element_if_clickable(PL.BUTTON_PROFILE_PAGE)
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
