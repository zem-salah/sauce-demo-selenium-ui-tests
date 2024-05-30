from behave import then


@then('he should be on sauce lab products page')
def step_impl(context):
    context.page.page_is_visible()
