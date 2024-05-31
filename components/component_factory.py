from components.primary_header import PrimaryHeader
from components.product_tile import ProductTile
from components.secondary_header import SecondaryHeader
from components.inventory_container import InventoryContainer
from components.footer import Footer


class ComponentFactory:

    def __init__(self, driver):
        self._driver = driver

    def create_footer(self):
        return Footer(self._driver)

    def create_inventory_container(self):
        return InventoryContainer(self._driver)

    def create_primary_header(self):
        return PrimaryHeader(self._driver)

    def create_product_tile(self, product_pretty_name):
        return ProductTile(self._driver, product_pretty_name)

    def create_secondary_header(self):
        return SecondaryHeader(self._driver)
