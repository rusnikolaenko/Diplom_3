from selenium.webdriver.common.by import By


class RecoveryLocators:
    """ Наименование "Восстановить пароль" """
    TITLE = (By.XPATH, '//*[text() = "Восстановление пароля"]')

    """ Поле ввода "Email" """
    FILED_EMAIL = (By.XPATH, '//*[@name = "name"]')

    """ Поле ввода "Пароль" """
    FIELD_PASSWORD = (By.XPATH, '//*[@name="Введите новый пароль"]')

    """ Признак активности обводки поля ввода "Пароль" """
    FILED_STROKE_ACTIVE_PASSWORD = (By.XPATH, ".//div[contains(@class,'input_status_active')]")

    """ Признак активности поля ввода "Пароль" """
    FIELD_ACTIVE_PASSWORD = (By.XPATH, ".//label[contains(@class,'input__placeholder-focused')]")

    """Кнопка "Восстановить" """
    BUTTON_RECOVERY = (By.XPATH, '//*[text() = "Восстановить"]')

    """ Кнопка "Показать/скрыть" """
    BUTTON_SHOW_HIDE = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[name()='svg']")
