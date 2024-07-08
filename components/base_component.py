from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseComponent:

    def __init__(self, driver):
        self._driver = driver

    def enter_text(self, locator, text):
        """
        Basic method to enter a text in a filed located by locator.
        :param locator: used to find the element
        :param text: text to enter the field
        :return: None
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def find_element(self, locator):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(locator))

    def button_to_be_clickable(self, locator):
        return WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(locator))
