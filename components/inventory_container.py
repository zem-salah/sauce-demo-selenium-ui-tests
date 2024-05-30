from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryContainer:

    def __init__(self, driver):
        self._driver = driver

    def is_visible(self):
        return len(WebDriverWait(self._driver, 10).until(
            EC.visibility_of_any_elements_located(
                (By.XPATH, '//div[@data-test="inventory-list"]'
                           '//div[@data-test="inventory-item"]'))
        )) != 0
