from behave import when

from page_object.page_factory import PageFactory

"""
This file contains steps that can be performed on pages when user is logged 
in, but are not specific to a page.
"""


@when('he goes to the cart to checkout')
def step_impl(context):
    context.page.primary_header.click_on_cart()
    context.page = PageFactory(context.driver)("your cart")
