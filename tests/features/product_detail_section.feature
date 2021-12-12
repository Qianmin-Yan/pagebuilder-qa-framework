@ui @product_detail
Feature: The user is able to show product detail in page

  Background:
    Given I navigate to PageBuilder website with valid credential
    Then I should see the PageBuilder logo

  Scenario Outline: The user is able to show product detail in regular or home page
    Given the user click on menu "<page_type>"
    When the user add product detail into the first "<page_type>" with random product
    Then the user should see the Published successfully modal pop up
    And the user is able to see the same product in "<page_type>"
    Examples:
      | page_type        |
      | Regular pages    |
      | Home page        |
      | Collection pages |

  Scenario: The user is able to show product detail in product page
    Given the user click on menu "Product pages"
    When the user add product detail into the first product page with random product
    Then the user should see the Published successfully modal pop up
    And the user is able to see the same product in "Product pages"
  Scenario Outline: The user is able to show product detail in collection or product page
    Given the user click on menu "<page_type>"
    When the user add product detail into the first "<page_type>" with random product
    Then the user should see the Published successfully modal pop up
    And the user is able to see the same product in live page
    Examples:
      | page_type     |
      | Regular pages |
      | Home page     |
