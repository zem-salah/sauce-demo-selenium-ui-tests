from selenium.webdriver.common.by import By

from page_object.logged_in_base_page import LoggedInBasePage


class CheckoutCompletePage(LoggedInBasePage):

    """
    page object for checkout first step.
    https://www.saucedemo.com/checkout-complete.html
    """

    back_to_products_btn = (By.ID, 'back-to-products')

    def __init__(self, driver):
        super().__init__(driver)

    def page_is_visible(self):
        return self.base_component.find_element(
            self.back_to_products_btn).is_displayed()
