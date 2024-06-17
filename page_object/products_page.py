from data.products import Product
from page_object.logged_in_base_page import LoggedInBasePage


class ProductsPage(LoggedInBasePage):

    """
    Main page after login. https://www.saucedemo.com/inventory.html
    It is composed of product tiles.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.footer = self.component_factory("footer")
        self._products_tiles = {}

    def page_is_visible(self):
        product_tile = self.component_factory(
            "product tile", "Sauce Labs Backpack")
        return all((self.primary_header.is_visible(),
                    self.secondary_header.is_visible(),
                    product_tile.is_visible(),
                    self.footer.is_visible())
                   )

    def product_tiles(self, product: Product):
        if product.name not in self._products_tiles:
            self._products_tiles[product.name] = self.component_factory(
                "product tile", product)
        return self._products_tiles[product.name]
