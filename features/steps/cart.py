from behave import then
from robber import expect, BadExpectation

from utils.session_manager import Session


@then('"{product_pretty_name}" product is in the cart')
def step_impl(context, product_pretty_name):
    product_in_cart = context.current_session.get(Session.CART)
    try:
        expect(context.page.cart_item(product_in_cart).is_visible())\
            .to.be.true()
    except BadExpectation as e:
        e.message = f'Product {product_pretty_name} is not in the cart'
        raise e
