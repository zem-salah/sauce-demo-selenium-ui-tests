from components.base_component import BaseComponent


class Footer(BaseComponent):

    def __init__(self, driver):
        super().__init__(driver)

    def is_visible(self):
        return True
