from page_object.base_page import BasePage
from page_object.logged_in_base_page import LoggedInBasePage


class ProductsPage(LoggedInBasePage):

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

    def product_tiles(self, product_pretty_name):
        if product_pretty_name not in self._products_tiles:
            self._products_tiles[product_pretty_name] = self\
                .component_factory("product tile", product_pretty_name)
        return self._products_tiles[product_pretty_name]
