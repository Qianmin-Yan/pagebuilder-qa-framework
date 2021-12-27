@ui @image

Feature: The user is able to upload image and see it in live page

  Background:
    Given I navigate to PageBuilder website with valid credential
    Then I should see the PageBuilder logo

  Scenario: The user is able to upload image and see it in live page
    Given the user add image with link "https://www.google.com/" into the first regular page
    Then the user should see the Published successfully modal pop up
    Then the user should see the image shows
    And the user will be redirected to "https://www.google.com/" in current page when clicking on image



