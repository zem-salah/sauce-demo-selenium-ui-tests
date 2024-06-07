from page_object.cart_page import CartPage
from page_object.login import Login
from page_object.products_page import ProductsPage


class PageFactory:

    def __init__(self, driver):
        self._driver = driver

    def __call__(self, page_name):
        page_name_to_creation_function = {
            'login': self._create_login_page,
            'products': self._create_products_page,
            'your cart': self._create_your_cart_page,
        }
        page_method = page_name_to_creation_function.get(page_name)
        if page_method:
            return page_method()
        else:
            raise ValueError(f"Page {page_name} not found")

    def _create_login_page(self):
        return Login(self._driver)

    def _create_products_page(self):
        return ProductsPage(self._driver)

    def _create_your_cart_page(self):
        return CartPage(self._driver)
