
from behave import given, when
from robber import expect

from data.user import UserData
from page_object.page_factory import PageFactory
from utils.session_manager import Session


@given('sauce demo login form is visible')
def step_impl(context):
    context.page = PageFactory(context.driver)("login")
    context.page.navigate()
    expect(context.page.page_is_visible()).to.be.true()


@given('"{user_pretty_name}" is logged in and is on the "{page_pretty_name}" page')
def step_impl(context, user_pretty_name, page_pretty_name):
    context.page = PageFactory(context.driver)(page_pretty_name)
    context.driver.get(context.page.BASE_URL)
    context.driver.add_cookie({
        'name': 'session-username',
        'value': UserData.get_user_name(user_pretty_name),
    })
    context.page.navigate()
    context.execute_steps(
        f'Then he should be on "{page_pretty_name}" page'
    )
    context.current_session = Session()


@when('"{user_pretty_name}" logs in')
def step_impl(context, user_pretty_name):
    user_name = UserData.get_user_name(user_pretty_name)
    password = UserData.get_user_password(user_pretty_name)
    context.page = context.page.login(user_name, password)
    context.current_session = Session()
