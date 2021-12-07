Feature: The user is able to submit form with or without form

#  Scenario: The user is able to submit form with coupon
#    Given the user add form with coupon into the first regular page
#    Then the user should see the Published successfully modal pop up
#    When the user submit form with "qm.yan@aftership.com"
#    Then the user should see the coupon "test" is shown

  Scenario: The user is able to submit form without coupon
    Given the user visit the page "https://qianmin-pagebuilder-testing-store.myshopify.com/pages/page-25"
    When the user submit form with "qm.yan@aftership.com"
#    Then the user should see the message "Thanks for subscribing" shows


