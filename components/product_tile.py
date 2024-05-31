from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from data.products_page import ProductsData


class ProductTile(BaseComponent):

    def __init__(self, driver, product_pretty_name):
        super().__init__(driver)
        self.product_pretty_name = product_pretty_name

    @property
    def add_to_cart_btn(self):
        product_locator_value = ProductsData.get_product_locator_value(
            self.product_pretty_name)
        return By.CSS_SELECTOR, '[data-test=add-to-cart-' \
                                + product_locator_value + ']'

    def is_visible(self):
        pass

    def add_to_cart(self):
        self.click_on_button(self.add_to_cart_btn)
