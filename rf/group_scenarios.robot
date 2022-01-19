*** Settings ***
Library             rf.AddressBook
Library             Collections
Suite Setup         Init Fixtures
Suite Teardown      Destroy Fixtures


*** Test Cases ***
Add new group
    ${old_list}=                    Get Groups List
    ${group}=                       New Group               name1            header1           footer1
    Create Group                    ${group}
    ${new_list}=                    Get Groups List
    Append To List                  ${old_list}             ${group}
    Lists Should Be Equal           ${new_list}             ${old_list}

Edit group
    ${old_list}=                    Get Groups List
    ${len}=                         Get Length              ${old_list}
    ${index}=                       Evaluate                random.randrange(${len})           random
    ${selected_group}=              Get From List           ${old_list}      ${index}
    ${new_group}=                   New Group Edited        ${index}         name_edited      header_edited     footer_edited
    Edit Group                      ${selected_group}       ${new_group}
    ${new_list}=                    Get Groups List
    Remove Values From List         ${old_list}             ${selected_group}
    Append To List                  ${old_list}             ${new_group}
    Sorted Lists Should Be Equal    ${new_list}             ${old_list}

Delete group
    ${old_list}=                    Get Groups List
    ${len}=                         Get Length              ${old_list}
    ${index}=                       Evaluate                random.randrange(${len})           random
    ${group}=                       Get From List           ${old_list}      ${index}
    Delete Group                    ${group}
    ${new_list}=                    Get Groups List
    Remove Values From List         ${old_list}             ${group}
    Lists Should Be Equal           ${new_list}             ${old_list}

