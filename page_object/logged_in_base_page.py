from page_object.base_page import BasePage
from urllib.parse import urljoin


class LoggedInBasePage(BasePage):

    """
    base page for web pages after logging in. Thes pages have header and
    footer in common
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.primary_header = self.component_factory('primary header')
        self.secondary_header = self.component_factory('secondary header')

    def navigate(self, cookie_name=None, cookie_value=None):
        if cookie_name and cookie_value:
            self.driver.add_cookie({
                'name': cookie_name,
                'value': cookie_value,
            })
        self.driver.get(urljoin(self.BASE_URL, self.path))
