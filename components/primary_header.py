from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class PrimaryHeader(BaseComponent):

    shopping_cart_link = (By.XPATH, '//*[@data-test="shopping-cart-link"]')

    def __init__(self, driver):
        super().__init__(driver)

    def is_visible(self):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//div[@data-test="primary-header"]'
                           '//a[@data-test="shopping-cart-link"]'))
        ).is_displayed()

    def get_number_products_in_cart(self):
        return self.find_element(self.shopping_cart_link).find_element(
            By.XPATH, '//*[@data-test="shopping-cart-badge"]').text

    def click_on_cart(self):
        self.click(self.shopping_cart_link)
