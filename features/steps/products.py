from behave import when, then
from robber import expect, BadExpectation

from data.products import Product
from utils.session_manager import SessionData


@when('he adds "{product_pretty_name}" product to cart')
def step_impl(context, product_pretty_name):
    product = Product(product_pretty_name)
    context.page.product_tiles(product).add_product_to_cart()
    context.current_user.session(SessionData.CART).set(product)


@then('the add to cart button for product "{product_pretty_name}" '
      'turns into remove button')
def step_impl(context, product_pretty_name):
    try:
        expect(context.page.product_tiles(Product(product_pretty_name))
               .is_remove_button_displayed()).to.be.true()
    except BadExpectation as e:
        e.message = 'Remove button is not displayed'
        raise e
