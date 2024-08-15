from selenium.webdriver.common.by import By

from data.products import Product
from page_object.logged_in_base_page import LoggedInBasePage


class CheckoutOverviewPage(LoggedInBasePage):

    """
    page object for checkout first step.
    https://www.saucedemo.com/checkout-step-two.html
    """

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def path(self):
        return '/checkout-step-two.html'

    def page_is_visible(self):
        pass
