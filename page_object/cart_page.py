from data.products import Product
from page_object.logged_in_base_page import LoggedInBasePage


class CartPage(LoggedInBasePage):

    """
    page object for cart page. https://www.saucedemo.com/cart.html
    This page is composed of cart items representing product added in cart
    by the user
    """

    def __init__(self, driver):
        super().__init__(driver)
        self._cart_items = {}

    @property
    def path(self):
        return '/cart.html'

    def page_is_visible(self):
        pass

    def cart_item(self, product: Product):
        if product.name not in self._cart_items:
            self._cart_items[product.name] = self.component_factory(
                "cart item", product)
        return self._cart_items[product.name]
