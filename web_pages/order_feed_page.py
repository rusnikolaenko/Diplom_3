import allure
from selenium.common import StaleElementReferenceException

from data import Urls
from web_pages.base_page import BasePage
from web_locators.order_feed_locators import OrderPageLocators as OPL

class OrderFeedPage(BasePage):

    @allure.step('Открытие страницы "Лента заказов"')
    def open_page(self):
        self.open_url(Urls.MAIN_PAGE + Urls.FEED_PAGE)

    @allure.step('Нажатие на сущность заказа в ленте')
    def click_order_object(self):
        self.click_element_if_clickable(OPL.ORDER_OBJECT)

    @allure.step("Проверка нахождения идентификатора заказа в ленте")
    def found_order_at_feed(self, order_id):
        try:
            elements = self.find_until_all_elements_located(OPL.ORDERS_AT_FEED)
            for element in elements:
                if order_id in element.text:
                    return True
        except StaleElementReferenceException:
            # Повторный поиск элементов
            elements = self.find_until_all_elements_located(OPL.ORDERS_AT_FEED)
            for element in elements:
                if order_id in element.text:
                    return True
        return False

    @allure.step('Проверка открытия окна заказа')
    def check_order_window(self):
        return self.check_presence(OPL.ORDER_STRUCTURE).is_displayed()

    @allure.step('Получение кол-ва заказов за сегодня')
    def get_total_count_today(self):
        self.find_element_visibility(OPL.TOTAL_COUNT_TODAY)
        return self.get_text(OPL.TOTAL_COUNT_TODAY)
