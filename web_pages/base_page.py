from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    '''Найти видимый элемент'''
    def find_element_visibility(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                         message=f'Cant find element by locator {locator}')

    '''Найти кликабельный элемент'''
    def find_element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         message=f"Can't find element by locator {locator}")

    '''Найти невидимый элемент'''
    def find_element_not_visibility(self, locator, timeout=60):
        return WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")

    '''Вставить текст'''
    def set_text(self, locator, text):
        element = self.find_element_visibility(locator)
        element.send_keys(text)

    '''Получить текст'''
    def get_text(self, locator):
        element = self.find_element_visibility(locator)
        return element.text

    '''Кликнуть видимый элемент'''
    def click_element_if_visibility(self, locator):
        element = self.find_element_visibility(locator)
        element.click()

    '''Кликнуть элемент'''
    def click_element_if_clickable(self, locator):
        click_element = self.find_element_visibility(locator)
        self.driver.execute_script('arguments[0].click();', click_element)

    '''Открыть ссылку'''
    def open_url(self, url):
        self.driver.get(url)

    '''Получить ссылку'''
    def get_url(self):
        return self.driver.current_url

    '''Проверить существующий элемент'''
    def check_exist_element(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    '''Перетащить элемент'''
    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()
        self.driver.execute_script("""
        var source = arguments[0];
        var target = arguments[1];
        var evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        source.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        source.dispatchEvent(evt);""",
        draggable, droppable)
        
    '''Проверить невидимость элемента'''
    def check_invisibility(self, locator) -> object:
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    '''Проверить присутствие элемента на странице'''
    def check_presence(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    '''Нахождение нескольких элементов'''
    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))
