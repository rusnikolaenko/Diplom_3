from selenium.webdriver.common.by import By


class OrderPageLocators:
    """ Заголовок на странице "лента заказов" """
    TITLE_ORDER_PAGE = (By.XPATH, '//*[text() = "Лента заказов"]')

    """ Сущность в ленте заказов """
    ORDER_OBJECT = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')

    """ Текст "Состав" в окне сущности  """
    ORDER_STRUCTURE = By.XPATH, '//*[text()="Cостав"]'

    """ Заказы в ленте заказов """
    ORDERS_AT_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                "text_type_digits-default']")

    """ Счетчик заказов за сегодня """
    TOTAL_COUNT_TODAY = (By.XPATH, '//*[text() = "Выполнено за сегодня:"]/following::*[@class][1]')
