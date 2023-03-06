Feature: Add Book Verification
  @smoke
  Scenario: Verify Add book API functionality
    Given book details needs to be added
    When we execute the add book
    Then book is successfully added


  @regression
  Scenario Outline: Verify Add book API functionality
    Given book details needs to be added
    When we execute the add book with <isbn> and <aisle> number
    Then book is successfully added
    Examples:
      | isbn | aisle |
      | junee | 2022  |
      | julye | 2022  |
#      | augu | 2022  |
#      | sept | 2022  |
#      | octo | 2022  | /Users/jithin/IdeaProjects/python