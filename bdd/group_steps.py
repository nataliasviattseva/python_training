from pytest_bdd import given, when, then
from model.group import Group
import random


@given("a group list", target_fixture="group_list")
def group_list(db):
    return db.get_groups_list()


@given("a group with <name>, <header> and <footer>", target_fixture="new_group")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when("I add the group to the list")
def add_new_group(app, new_group):
    app.group.create_group(new_group)


@then("the new group list is equal to the old list with the added group")
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_groups_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given("a group with <edit_name>, <edit_header> and <edit_footer>", target_fixture="edited_group")
def edited_group(edit_name, edit_header, edit_footer):
    return Group(name=edit_name, header=edit_header, footer=edit_footer)


@given("a selected group", target_fixture="selected_group")
def selected_group(group_list):
    return random.choice(group_list)


@when("I edit the group")
def edit_group(app, selected_group, edited_group):
    edited_group.id = selected_group.id
    app.group.edit_group_by_id(selected_group.id, edited_group)


@then("the group list is equal to the old list with the edited group")
def verify_group_edited(db, group_list, selected_group, edited_group):
    old_groups = group_list
    new_groups = db.get_groups_list()
    old_groups.remove(selected_group)
    old_groups.append(edited_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@when("I delete the group")
def delete_group(app, selected_group):
    app.group.delete_group_by_id(selected_group.id)


@then("the new group list is equal to the old list with the deleted group")
def verify_group_deleted(db, group_list, selected_group):
    old_groups = group_list
    new_groups = db.get_groups_list()
    old_groups.remove(selected_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
