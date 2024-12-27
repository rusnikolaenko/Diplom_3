import allure
from web_pages.main_page import MainPage
from web_pages.profile_page import ProfilePage

class TestMainPage:

    @allure.title('Открытие страницы "Конструктор"')
    def test_open_constructor(self, driver):
        mp = MainPage(driver)
        mp.open_reg_page()
        mp.click_constructor_button()
        assert mp.check_title_constructor() is True, 'Не удалось перейти на страницу "Конструктор"'

    @allure.title('Открытие страницы "Лента заказов"')
    def test_open_order_feed(self, driver):
        mp = MainPage(driver)
        mp.open_reg_page()
        mp.click_order_feed_button()
        assert mp.check_title_order_feed() is True, 'Страница "Лента заказов" не открыта'

    @allure.title('Открытие окна ингредиента')
    def test_open_window_ingredient(self, driver):
        mp = MainPage(driver)
        mp.open_main_page()
        mp.click_ingredient_r2_d3()
        assert mp.check_clickable_order_button() is True, 'Окно ингредиента не открыто'

    @allure.title('Закрытие окна ингредиента')
    def test_close_window_ingredient(self, driver):
        mp = MainPage(driver)
        mp.precondition_close_window()
        mp.click_close_button()
        assert mp.check_clickable_order_button() is True, 'Окно ингредиента не закрыто'

    @allure.title('Проверка изменения счетчика ингредиента')
    def test_counter_add_ingredient(self, driver):
        mp = MainPage(driver)
        mp.open_main_page()
        pre_result = mp.get_count_value()
        mp.add_filling_to_order()
        post_result = mp.get_count_value()
        assert pre_result < post_result, 'Счетчик не изменился'

    @allure.title('Проверка возможности оформить заказ авторизованным пользователем')
    def test_placing_order(self, driver, test_data):
        pl = ProfilePage(driver)
        mp = MainPage(driver)

        pl.authorization(test_data)
        mp.add_filling_to_order()
        mp.click_order_button()
        assert mp.check_placing_order() == 'идентификатор заказа', 'Оформить заказ не удалось'
