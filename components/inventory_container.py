from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class InventoryContainer(BaseComponent):

    def __init__(self, driver):
        super().__init__(driver)

    def is_visible(self):
        return len(WebDriverWait(self._driver, 10).until(
            EC.visibility_of_any_elements_located(
                (By.XPATH, '//div[@data-test="inventory-list"]'
                           '//div[@data-test="inventory-item"]'))
        )) != 0
