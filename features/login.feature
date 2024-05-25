Feature: Login Functionality

  @try
  Scenario Outline: Login with Valid Credentials
    Given I navigate to Login Page
    When I entered valid UserName as "<userName>"
    And I entered valid Password as "<passWord>"
    And I click on Login button
    Then App should be Opened for User
    Examples:
    |userName                     |passWord           |
    |          |     |

