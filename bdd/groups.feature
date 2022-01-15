Feature: Scenario outlines
  Scenario Outline: Add new group
    Given a group list
    Given a group with <name>, <header> and <footer>
    When I add the group to the list
    Then the new group list is equal to the old list with the added group

    Examples:
    | name  | header  | footer  |
    | name1 | header1 | footer1 |
    | name2 | header2 | footer2 |


  Scenario Outline: Edit the group
    Given a group list
    Given a selected group
    Given a group with <edit_name>, <edit_header> and <edit_footer>
    When I edit the group
    Then the group list is equal to the old list with the edited group

    Examples:
    | edit_name     | edit_header     | edit_footer     |
    | name_edited_1 | header_edited_1 | footer_edited_1 |
    | name_edited_2 | header_edited_2 | footer_edited_2 |


  Scenario Outline: Delete the group
    Given a group list
    Given a selected group
    When I delete the group
    Then the new group list is equal to the old list with the deleted group



