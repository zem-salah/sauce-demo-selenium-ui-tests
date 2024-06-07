Feature: Login to sauce demo web site as standard user
  In order to access sauce demo website
  As standard user
  I need to be able to login

  Scenario: login as standard user
    Given sauce demo login form is visible
    When "standard user" logs in
    Then he should be on "products" page