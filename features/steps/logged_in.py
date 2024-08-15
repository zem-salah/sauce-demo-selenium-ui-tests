from behave import when

from features.steps.generic_steps import click_and_navigate_to_page

"""
This file contains steps that can be performed on pages when user is logged 
in, but are not specific to a page.
"""


@when('he goes to the cart to checkout')
def step_impl(context):
    click_and_navigate_to_page(context, 'cart', 'your cart')
