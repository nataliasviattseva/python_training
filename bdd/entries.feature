Feature: Scenario outlines
  Scenario Outline: Add new entry
    Given an entry list
    Given an entry with <first_name> and <last_name>
    When I add the entry to the list
    Then the new entry list is equal to the old list with the added entry

    Examples:
    | first_name   | last_name   |
    | first_name_1 | last_name_1 |
    | first_name_2 | last_name_2 |


  Scenario Outline: Edit the entry
    Given an entry list
    Given a selected entry
    Given an entry with <edit_first_name> and <edit_last_name>
    When I edit the entry
    Then the entry list is equal to the old list with the edited entry

    Examples:
    | edit_first_name     | edit_last_name     |
    | first_name_edited_1 | last_name_edited_1 |
    | first_name_edited_2 | last_name_edited_2 |


  Scenario Outline: Delete the entry
    Given an entry list
    Given a selected entry
    When I delete the entry
    Then the new entry list is equal to the old list with the deleted entry



