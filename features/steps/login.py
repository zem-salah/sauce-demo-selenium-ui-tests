from behave import given, when
from robber import expect

from data.user import UserData
from page_object.page_factory import PageFactory
from utils.session_manager import Session


@given('sauce demo login form is visible')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    context.page = PageFactory(context.driver)("login")
    expect(context.page.page_is_visible()).to.be.true()


@when('"{user_pretty_name}" logs in')
def step_impl(context, user_pretty_name):
    user_name = UserData.get_user_name(user_pretty_name)
    password = UserData.get_user_password(user_pretty_name)
    context.page = context.page.login(user_name, password)
    context.current_session = Session()
