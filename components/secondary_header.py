from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecondaryHeader:

    def __init__(self, driver):
        self._driver = driver

    def is_visible(self):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//div[@data-test="secondary-header"]'
                           '//select[@data-test="product-sort-container"]'))
        ).is_displayed()
