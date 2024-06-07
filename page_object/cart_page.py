from page_object.logged_in_base_page import LoggedInBasePage


class CartPage(LoggedInBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.product_items = {}

    def page_is_visible(self):
        pass
