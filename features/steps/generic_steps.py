from behave import then
from robber import expect

from page_object.page_factory import PageFactory

"""
This file contains steps that are low level and common to all pages.
"""


@then('he should be on "{page_pretty_name}" page')
def step_impl(context, page_pretty_name):
    expected_page = PageFactory(context.driver)(page_pretty_name)
    expect(isinstance(context.page, type(expected_page))).to.be.true()
    context.page.page_is_visible()
