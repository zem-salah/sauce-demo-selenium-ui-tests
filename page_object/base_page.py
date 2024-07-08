from components.base_component import BaseComponent
from components.component_factory import ComponentFactory


class BasePage:

    """
    base page containing driver, component factory and in instance of a base
    component. From a composition POV, we can say that a base page is composed
    of a base component.
    """

    BASE_URL = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver
        self.component_factory = ComponentFactory(driver)
        self.base_component = BaseComponent(driver)

    def get_field_locator_by_pretty_name(self, field_pretty_name):
        return self.field_pretty_name_to_locator.get(field_pretty_name)
