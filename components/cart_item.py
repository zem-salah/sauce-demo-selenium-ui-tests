from components.base_component import BaseComponent
from data.products import Product


class CartItem(BaseComponent):

    """
    Component representing a product in a cart. Used by cart page.
    We give it a Product instance that contains data of the product
    that this item display.
    """

    def __init__(self, driver, product: Product):
        super().__init__(driver)
        self.product = product

    def is_visible(self):
        return True
