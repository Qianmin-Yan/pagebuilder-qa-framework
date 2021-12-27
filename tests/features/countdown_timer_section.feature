@ui @countdown_timer

Feature: The user is able to see countdown timer in live page

  Background:
    Given I navigate to PageBuilder website with valid credential
    Then I should see the PageBuilder logo

  Scenario: The user is able to see countdown timer in live page
    Given the user add countdown timer into the first regular page
    Then the user should see the Published successfully modal pop up
    Then the user should see the countdown timer shows


