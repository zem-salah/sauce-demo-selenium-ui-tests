from behave import then, when
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


@when("he fills")
def step_impl(context):
    """
    Generic step to fill a form from a table composed of two columns
    '|field|value|'

    Each row in this table will be used to fill one field in the form.

    'field' column, must contain pretty names of the fields to fill.
    Exemple :
        |field      |value        |
        |user name  | new user    |
        |address    | foo         |
        |email      | bar@foo.com |
        ...
    """
    for row in context.table:
        context.page.base_component.enter_text(
            context.page.get_field_locator_by_pretty_name(row['field']),
            row['value']
        )


@when('the user clicks on "{element_pretty_name}"')
def click(context, element_pretty_name):
    """
    Generic step to click on an element of the page identified by its pretty
    name.
    """
    context.page.base_component.click(
        context.page.get_field_locator_by_pretty_name(element_pretty_name)
    )


@when('clicks on "{element_pretty_name}" to navigate to "{page_pretty_name}" page')
def click_and_navigate_to_page(context, element_pretty_name, page_pretty_name):
    """
    Generic step to click on an element of the page identified by its pretty
    name. The click take the user to another page.
    """
    click(context, element_pretty_name)
    context.page = PageFactory(context.driver)(page_pretty_name)
