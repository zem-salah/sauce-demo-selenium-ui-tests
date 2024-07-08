
from behave import given, when
from robber import expect

from data.user import User
from page_object.page_factory import PageFactory


@given('sauce demo login form is visible')
def step_impl(context):
    context.page = PageFactory(context.driver)("login")
    context.page.navigate()
    expect(context.page.page_is_visible()).to.be.true()


@given('"{user_pretty_name}" is logged in and is on the "{page_pretty_name}" '
       'page')
def step_impl(context, user_pretty_name, page_pretty_name):
    context.page = PageFactory(context.driver)(page_pretty_name)
    context.driver.get(context.page.BASE_URL)
    context.current_user = User(user_pretty_name)
    context.page.navigate(cookie_name='session-username',
                          cookie_value=context.current_user.name)
    context.execute_steps(
        f'Then he should be on "{page_pretty_name}" page'
    )


@when('"{user_pretty_name}" logs in')
def step_impl(context, user_pretty_name):
    context.current_user = User(user_pretty_name)
    context.page = context.page.login(
        context.current_user.name, context.current_user.password)
