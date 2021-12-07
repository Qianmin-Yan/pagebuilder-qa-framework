Feature: The user is able to show product list in page

  Scenario Outline: The user is able to show product list in page
    Given the user navigate to "<page_type>"
    When the user add product list into the first "<page_type>" with "<added_products_total>" products
    Then the user should see the Published successfully modal pop up
    And the user is able to see "<added_products_total>" product in live page product list section
    Examples:
      | page_type     | added_products_total |
      | Regular pages | 1                    |
      | Home page     | 2                    |
      | Product pages | 3                    |