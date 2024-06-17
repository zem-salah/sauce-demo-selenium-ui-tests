class ProductsData:

    _translate = {
        "Sauce Labs Backpack": "sauce-labs-backpack"
    }

    @classmethod
    def get_product_locator_value(cls, product_pretty_name):
        try:
            return cls._translate[product_pretty_name]
        except KeyError:
            raise KeyError(
                f'Product {product_pretty_name} does not exist.'
            )
