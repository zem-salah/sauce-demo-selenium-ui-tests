from behave import then, when
from robber import expect, BadExpectation

from page_object.page_factory import PageFactory
from utils.session_manager import SessionData


@when('the user proceed to checkout')
def step_impl(context):
    context.page.checkout()
    context.page = PageFactory(context.driver)("checkout information")


@then('"{product_pretty_name}" product is in the cart')
def step_impl(context, product_pretty_name):
    product_in_cart = context.current_user.session(
        SessionData.CART).get(product_pretty_name)
    try:
        expect(context.page.cart_item(product_in_cart).is_visible())\
            .to.be.true()
    except BadExpectation as e:
        e.message = f'Product {product_pretty_name} is not in the cart'
        raise e
