@ui @product_detail
Feature: The user is able to see product detail in page

  Background:
    Given I navigate to PageBuilder website with valid credential
    Then I should see the PageBuilder logo

  Scenario Outline: The user is able to see product detail in regular or home page and interact with buttons
    Given the user click on menu "<page_type>"
    When the user add product detail into the blank "<page_type>" with random product
    Then the user should see the Published successfully modal pop up
    And the user is able to see the same product in "<page_type>"
    When the user click on "Add to cart"
    Then the product appeared in cart
    When the user click on "Buy it now"
    Then the user is navigated to checkout page
    Examples:
      | page_type        |
      | Regular pages    |
      | Home page        |
      | Product pages    |
      | Collection pages |
      | Blog post pages  |

  Scenario: The user is able to see countdown timer in product detail
    Given the user click on menu "Regular pages"
    When the user add product detail with countdown timer into the blank "Regular pages" with random product
    Then the user should see the Published successfully modal pop up
    And the user is able to see the same product in "Regular pages"
    And the user see the countdown timer shows