from components.base_component import BaseComponent
from components.component_factory import ComponentFactory


class BasePage:

    """
    base page containing driver, component factory and in instance of a base
    component. From a composition POV, we can say that a base page is composed
    of a base component.
    """

    def __init__(self, driver):
        self.driver = driver
        self.component_factory = ComponentFactory(driver)
        self.base_component = BaseComponent(driver)
