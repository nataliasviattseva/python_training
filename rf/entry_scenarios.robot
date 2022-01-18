*** Settings ***
Library             rf.AddressBook
Library             Collections
Suite Setup         Init Fixtures
Suite Teardown      Destroy Fixtures


*** Test Cases ***
Add new entry
    ${old_list}=                    Get Entries List
    ${entry}=                       New Entry               first_name            last_name
    Create Entry                    ${entry}
    ${new_list}=                    Get Entries List
    Append To List                  ${old_list}             ${entry}
    Lists Should Be Equal           ${new_list}             ${old_list}

Edit entry
    ${old_list}=                    Get Entries List
    ${len}=                         Get Length              ${old_list}
    ${index}=                       Evaluate                random.randrange(${len})           random
    ${selected_entry}=              Get From List           ${old_list}      ${index}
    ${new_entry}=                   New Entry               first_name_edited      last_name_edited
    Edit Entry                      ${selected_entry}       ${new_entry}
    ${new_list}=                    Get Entries List
    Remove Values From List         ${old_list}             ${selected_entry}
    Append To List                  ${old_list}             ${new_entry}
    Lists Should Be Equal           ${new_list}             ${old_list}

Delete entry
    ${old_list}=                    Get Entries List
    ${len}=                         Get Length              ${old_list}
    ${index}=                       Evaluate                random.randrange(${len})           random
    ${entry}=                       Get From List           ${old_list}      ${index}
    Delete Entry                    ${entry}
    ${new_list}=                    Get Entries List
    Remove Values From List         ${old_list}             ${entry}
    Lists Should Be Equal           ${new_list}             ${old_list}

