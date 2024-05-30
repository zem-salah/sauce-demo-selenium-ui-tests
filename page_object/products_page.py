from page_object.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.primary_header = self.component_factory.create_primary_header()
        self.secondary_header = self.component_factory\
            .create_secondary_header()
        self.inventory_container = self.component_factory\
            .create_inventory_container()
        self.footer = self.component_factory.create_footer()

    def page_is_visible(self):
        return all((self.primary_header.is_visible(),
                    self.secondary_header.is_visible(),
                    self.inventory_container.is_visible(),
                    self.footer.is_visible())
                   )
