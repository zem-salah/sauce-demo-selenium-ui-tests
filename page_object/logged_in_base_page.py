from page_object.base_page import BasePage


class LoggedInBasePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.primary_header = self.component_factory("primary header")
        self.secondary_header = self.component_factory("secondary header")
