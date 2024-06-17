from behave import when, then
from robber import expect, BadExpectation

from data.products import Product
from utils.session_manager import Session


@when('he adds "{product_pretty_name}" product to cart')
def step_impl(context, product_pretty_name):
    product = Product(product_pretty_name)
    context.page.product_tiles(product).add_product_to_cart()
    context.current_session.set(Session.CART, product)


@then('the add to cart button for product "{product_pretty_name}" '
      'turns into remove button')
def step_impl(context, product_pretty_name):
    try:
        expect(context.page.product_tiles(Product(product_pretty_name))
               .is_remove_button_displayed()).to.be.true()
    except BadExpectation as e:
        e.message = 'Remove button is not displayed'
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
