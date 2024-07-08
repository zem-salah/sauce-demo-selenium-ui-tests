from enum import Enum

from data.products import Product


class _CartData:

    def __init__(self):
        self._data = {}

    def set(self, product: Product):
        self._data[product.name] = product

    def get(self, product_name, default=None):
        return self._data.get(product_name, default)


class SessionData(Enum):
    CART = _CartData


class SessionRepository:
    """
        Entry point to session management. We want to have a simple API
        to ease readability. A session will be created when a new user object
        is instantiated.
    """

    def __init__(self):
        self._data = {}

    def __call__(self, session_type: SessionData):
        if session_type not in self._data:
            self._data[session_type] = session_type.value()
        return self._data.get(session_type)
