Feature: The user is able to show product list in page
  Background:
    Given I navigate to PageBuilder website with valid credential
    Then I should see the PageBuilder logo

  Scenario Outline: The user is able to show product list in page
    Given the user click on menu "<page_type>"
    When the user add product list into the first "<page_type>" with "<added_products_total>" products
    Then the user should see the Published successfully modal pop up
    And the user is able to see "<added_products_total>" product in live page product list section
    Examples:
      | page_type     | added_products_total |
      | Regular pages | 1                    |
      | Home page     | 2                    |
      | Product pages | 3                    |