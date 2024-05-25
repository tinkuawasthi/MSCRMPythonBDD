Feature: Search Functionality

  @search #creating tag for understanding
  Scenario: Search for a valid Product
    Given I got navigated to Home page
    When I entered valid product into Search box field
    And I click on Search button
    Then Valid product should be displayed in Search results

  @search #creating tag for understanding
  Scenario: Search for an invalid product
    Given I got navigated to Home page
    When I entered invalid product into Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results


  Scenario: Search without entering any search term for product
    Given I got navigated to Home page
    When I do not enter value into Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results