@ui @video

Feature: The user is able to add youtube video and manipulate it in live page

  Background:
    Given I navigate to PageBuilder website with valid credential
    Then I should see the PageBuilder logo

  Scenario Outline: The user is able to add youtube video and see it in live page
    When the user add youtube video with link "https://www.youtube.com/watch?v=cMPEd8m79Hw" into the first regular page
    And the user set the video display ratio "<display_ratio>" and display width "<display_width>
    Then the user should see the Published successfully modal pop up
    And the user should see the video shows
    And the user is able to play and pause the video in screen <viewport_size>
    Examples:
      | display_ratio | display_width | viewport_size                  |
      | 16:9          | Standard      | {"width": 1500, "height": 980} |
      | 16:9          | Large         | {"width": 1500, "height": 980} |
      | 4:3           | Standard      | {"width": 1500, "height": 980} |
      | 4:3           | Large         | {"width": 1500, "height": 980} |
      | 16:9          | Standard      | {"width": 414,  "height": 736} |
      | 4:3           | Large         | {"width": 414,  "height": 736} |

  Scenario Outline: The user is not able publish page with invalid youtube link
    When the user add youtube video with link "<link>" into the first regular page
    Then the user will be reminded if the link "<link>" "<is_valid>"
    Examples:
      | link                                         | is_valid |
      | https://www.youtube.com/watch?v=cMPEd8m79Hw  | valid    |
      | https://youtube.com/abc                      | invalid  |
      | https://youtu.be/yEz-E8l8vFo                 | valid    |
      | https://youtu.be/watch?=yEz-E8l8vFo          | invalid  |
      | https://www.youtube.com/watch??v=cMPEd8m79Hw | invalid  |
      | https://www.youtube.com/watch?vv=cMPEd8m79Hw | invalid  |
      | ""                                           | invalid  |