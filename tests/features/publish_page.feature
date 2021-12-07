Feature: The user is able to publish any kind of page from the template list

  Background:
    Given I navigate to website "/" with valid credential
    Then I should see the page title "Automizely Page Builder"

  Scenario Outline: The user is able to publish regular page or blog post page or home page
    Given the user click on menu "<page_type>"
    When the user choose from template "<template_name>" to publish "<page_type>"
    Then the user should see the Published successfully modal pop up
    Examples:
      | page_type       | template_name          |
      | Regular pages   | Christmas 01 page_list |
      | Blog post pages | Blog Post 02 page_list |
      | Home page       | New Year 01 page_list  |


  Scenario Outline: The user is able to publish product page
    Given the user click on menu "<page_type>"
    When the user choose template "<template_name>" to publish "<page_type>"
    Then the user should see the Published successfully modal pop up
    Examples:
      | page_type        | template_name                |
      | Product pages    | Christmas 02 page_list       |
      | Collection pages | Collection Page 01 page_list |

