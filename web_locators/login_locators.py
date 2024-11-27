from selenium.webdriver.common.by import By


class LoginLocators:
    """ Кнопка "Восстановить пароль" """
    BUTTON_RECOVERY_PASSWORD = (By.XPATH, '//*[text() = "Восстановить пароль"]')

    """ кнопка Войти """
    BUTTON_FOR_LOGIN = By.XPATH, '//button[text() = "Войти"]'

    """ кнопка Зарегистрироваться """
    BUTTON_FOR_REG = By.XPATH, '//button[text() = "Зарегистрироваться"]'

    """ поле ввода email на странице авторизации """
    FIELD_EMAIL_FOR_LOGIN = By.XPATH, '//*[@name = "name"]'

    """ поле ввода пароля на странице авторизации """
    FIELD_PASSWORD_FOR_LOGIN = By.XPATH, '//*[@name = "Пароль"]'

    """ Поле ввода имени на странице регистрации """
    FIELD_NAME_FOR_REG = By.XPATH, '//*[text()="Регистрация"]/following::*[@name = "name"][1]'

    """ Поле ввода Email на странице регистрации """
    FIELD_EMAIL_FOR_REG = (By.XPATH, '//*[text()="Регистрация"]/following::*[@name = "name"][2]')

    """ Поле ввода пароля на странице регистрации """
    FIELD_PASSWORD_FOR_REG = (By.XPATH, "//*[@name  = \"Пароль\"]")
