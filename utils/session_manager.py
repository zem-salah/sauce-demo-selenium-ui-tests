class Session:
    """
    First implem of Session. set and get don't take a lot of cases
    into account. This is a basic first implementation needed only for
    "add a product to cart". Respecting YAGNI principle, we do the minimun
    as we don't know what is coming next.
    I see this class evolving to an interface where each type of session
    (like cart) will handle its one mechanism of set, get, remove,...
    """
    CART = 'cart'

    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)




