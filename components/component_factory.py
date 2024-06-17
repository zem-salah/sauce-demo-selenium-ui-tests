from components.cart_item import CartItem
from components.primary_header import PrimaryHeader
from components.product_tile import ProductTile
from components.secondary_header import SecondaryHeader
from components.inventory_container import InventoryContainer
from components.footer import Footer


class ComponentFactory:

    def __init__(self, driver):
        self._driver = driver

    def __call__(self, component_name, *args, **kwargs):
        component_name_to_function_creation = {
            'footer': self._create_footer,
            'primary header': self._create_primary_header,
            'secondary header': self._create_secondary_header,
            'product tile': self._create_product_tile,
            'inventory container': self._create_inventory_container,
            'cart item': self._create_cart_item,
        }
        component_method = component_name_to_function_creation.get(
            component_name)
        if component_method:
            return component_method(*args, **kwargs) if args or kwargs else component_method()
        else:
            raise ValueError(f"Component {component_name} not found")

    def _create_cart_item(self, product):
        return CartItem(self._driver, product)

    def _create_footer(self):
        return Footer(self._driver)

    def _create_inventory_container(self):
        return InventoryContainer(self._driver)

    def _create_primary_header(self):
        return PrimaryHeader(self._driver)

    def _create_product_tile(self, product):
        return ProductTile(self._driver, product)

    def _create_secondary_header(self):
        return SecondaryHeader(self._driver)
