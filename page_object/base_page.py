from components.base_component import BaseComponent
from components.component_factory import ComponentFactory


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.component_factory = ComponentFactory(driver)
        self.base_component = BaseComponent(driver)
