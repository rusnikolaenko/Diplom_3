import allure
from web_pages.main_page import MainPage
from web_pages.order_feed_page import OrderFeedPage
from web_pages.profile_page import ProfilePage

class TestOrderFeed:

    @allure.title('Проверка открытия окна с информацией заказе')
    def test_open_order_window(self, driver):
        ofp = OrderFeedPage(driver)
        ofp.open_page()
        ofp.click_order_object()
        assert ofp.check_order_window() is True, 'Окно не открыто'

    @allure.title('Проверка совпадения id в ленте заказов и в истории заказов')
    def test_find_order_in_list(self, driver, test_data):
        pp = ProfilePage(driver)
        ofp = OrderFeedPage(driver)
        mp = MainPage(driver)

        pp.authorization(test_data)
        mp.add_filling_to_order()
        mp.click_order_button()
        order_id = mp.get_order_id()
        print(f"Order ID созданного заказа: {order_id}")  # Логирование
        mp.click_close_button()

        # Проверка в истории заказов
        pp.click_profile_page_button()
        pp.open_history_page()
        order_id_history = pp.found_order_at_history(order_id)
        print(f"Order ID в истории заказов: {order_id_history}")  # Логирование

        if not order_id_history:
            print("Ошибка: Заказ не найден в истории заказов. Проверьте синхронизацию данных.")

        # Проверка в ленте заказов
        mp.click_order_feed_button()
        order_id_order_feed = ofp.found_order_at_feed(order_id)
        print(f"Order ID в ленте заказов: {order_id_order_feed}")  # Логирование

        assert order_id_order_feed and order_id_history, 'Id не совпадают'

    @allure.title('Проверка изменения счетчика заказов за сегодня')
    def test_today_orders_counter(self, driver, test_data):
        pp = ProfilePage(driver)
        ofp = OrderFeedPage(driver)
        mp = MainPage(driver)

        pp.authorization(test_data)
        mp.click_order_feed_button()
        pre_count = ofp.get_total_count_today()
        mp.click_constructor_button()
        mp.add_filling_to_order()
        mp.click_order_button()
        mp.click_close_button()
        mp.click_order_feed_button()
        post_count = ofp.get_total_count_today()
        assert post_count > pre_count, 'Счетчик не изменился'

    @allure.title('Проверка появления только что созданного заказа в ленте заказов')
    def test_new_order_at_order_feed(self, driver, test_data):
        pp = ProfilePage(driver)
        ofp = OrderFeedPage(driver)
        mp = MainPage(driver)

        pp.authorization(test_data)
        mp.add_filling_to_order()
        mp.click_order_button()
        order_id = mp.get_order_id()
        print(f"Order ID созданного заказа: {order_id}")  # Логирование
        mp.click_close_button()

        # Проверка в ленте заказов
        mp.click_order_feed_button()
        assert ofp.found_order_at_feed(order_id) is True, f"Заказ с ID {order_id} не найден в ленте заказов"
