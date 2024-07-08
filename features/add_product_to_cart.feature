Feature: Add a product to cart as a standard user
  In order to purchase a product
  As standard user
  I need to be able to login, add the wanted product in cart and checkout

  Scenario: Journey scenario of buying a product from sauce labs demo web site as a standard user
    Given "standard user" is logged in and is on the "products" page
    Then he should be on "products" page

    When he adds "Sauce Labs Backpack" product to cart
    Then the cart should contain "1" product
    And the add to cart button for product "Sauce Labs Backpack" turns into remove button

    When he goes to the cart to checkout
    Then he should be on "your cart" page
    And "Sauce Labs Backpack" product is in the cart

    When the user proceed to checkout
    Then he should be on "checkout information" page

    When he fills
      |field        |value         |
      |first name   |standard_user |
      |last name    |user          |
      |postal code  |11111         |
#    And clicks on "continue"
#    Then he should be on "checkout overview" page
#
#    When the user clicks on "finish"
#    Then he should be on "checkout complete" page
