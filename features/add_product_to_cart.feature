Feature: Add a product to cart as a standard user
  In order to purchase a product
  As standard user
  I need to be able to add it to cart

  Scenario: add a product to cart
    Given "standard user" is logged in and is on the "products" page
    Then he should be on "products" page

    When he adds "Sauce Labs Backpack" product to cart
    Then the cart should contain "1" product
    And the add to cart button for product "Sauce Labs Backpack" turns into remove button

    When he goes to the cart to checkout
    Then he should be on "your cart" page
    And "Sauce Labs Backpack" product is in the cart