from behave import then


@When('he adds "{product_pretty_name}" product to cart')
def step_impl(context, product_pretty_name):


@then('he should be on sauce lab products page')
def step_impl(context):
    context.page.page_is_visible()

@then('the add to cart button turns into remove button')
def step_impl(context):


@then('the cart should contain "{number_products_in_cart}" product')
def step_impl(context, number_products_in_cart):

