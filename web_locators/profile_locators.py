from selenium.webdriver.common.by import By


class ProfileLocators:
    """ Кнопка Личный кабинет """
    BUTTON_PROFILE_PAGE = By.XPATH, '//*[@href = "/account"]'

    """ Кнопка "Личный кабинет" """
    BUTTON_PROFILE = By.XPATH, '//*[@href="/account/profile"]'

    """ Кнопка "История заказов" """
    BUTTON_HISTORY = By.XPATH, '//*[@href="/account/order-history"]'

    """ Кнопка "Выход" """
    BUTTON_EXIT = By.XPATH, '//*[@href="/account/order-history"]/following::*[@type="button"][1]'

    """ Заказы в "История заказов" """
    ORDERS_AT_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                   "'text_type_digits-default')]")
