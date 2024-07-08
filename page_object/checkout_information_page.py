from selenium.webdriver.common.by import By

from data.products import Product
from page_object.logged_in_base_page import LoggedInBasePage


class CheckoutInformationPage(LoggedInBasePage):

    """
    page object for checkout first step.
    https://www.saucedemo.com/checkout-step-one.html
    """

    first_name_txt = (By.XPATH, '//*[@data-test="firstName"]')
    last_name_txt = (By.XPATH, '//*[@data-test="lastName"]')
    postal_code_txt = (By.XPATH, '//*[@data-test="postalCode"]')
    continue_btn = (By.XPATH, '//*[@data-test="continue"]')

    page_elements_pretty_name_to_locator = {
        'first name': first_name_txt,
        'last name': last_name_txt,
        'postal code': postal_code_txt,
        'continue': continue_btn,
    }

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def path(self):
        return '/checkout-step-one.html'

    def page_is_visible(self):
        pass
