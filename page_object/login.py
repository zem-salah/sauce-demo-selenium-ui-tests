from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from page_object.products_page import ProductsPage


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_txt = (By.ID, "user-name")
    password_txt = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    def login(self, username, password):
        self.base_component.enter_text(self.username_txt, username)
        self.base_component.enter_text(self.password_txt, password)
        self.base_component.click_on_button(self.login_btn)
        return ProductsPage(self.driver)

    def page_is_visible(self):
        return all((
            self.base_component.find_element(self.username_txt).is_displayed(),
            self.base_component.find_element(self.password_txt).is_displayed(),
            self.base_component.button_to_be_clickable(
                self.login_btn).is_displayed())
        )
