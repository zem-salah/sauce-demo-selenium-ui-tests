from behave import then, when
from robber import expect, BadExpectation

from features.steps.generic_steps import click_and_navigate_to_page
from utils.session_manager import SessionData


@when('the user proceed to checkout')
def step_impl(context):
    click_and_navigate_to_page(context, 'checkout', 'checkout information')


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


@then('the cart should contain "{expected_number_products_in_cart}" product')
def step_impl(context, expected_number_products_in_cart):
    actual_number_product_in_cart = \
        context.page.primary_header.get_number_products_in_cart()
    try:
        expect(expected_number_products_in_cart).to.be.equal(
            actual_number_product_in_cart)
    except BadExpectation as e:
        e.message = f'Cart contains {actual_number_product_in_cart} ' \
                    f'product(s), expected {expected_number_products_in_cart}'
        raise e
