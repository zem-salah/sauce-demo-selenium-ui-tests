from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from data.products import ProductsData, Product


class ProductTile(BaseComponent):

    def __init__(self, driver, product: Product):
        super().__init__(driver)
        self.product = product

    @property
    def add_to_cart_btn(self):
        product_locator_value = ProductsData.get_product_locator_value(
            self.product.name)
        return By.CSS_SELECTOR, '[data-test=add-to-cart-' \
                                + product_locator_value + ']'

    @property
    def remove_from_cart_btn(self):
        """this button appears after clicking on add_to_cart_btn"""
        product_locator_value = ProductsData.get_product_locator_value(
            self.product.name)
        return By.CSS_SELECTOR, '[data-test=remove-' \
                                + product_locator_value + ']'

    def is_visible(self):
        pass

    def add_product_to_cart(self):
        self.click(self.add_to_cart_btn)

    def is_remove_button_displayed(self):
        return self.find_element(self.remove_from_cart_btn).is_displayed()
