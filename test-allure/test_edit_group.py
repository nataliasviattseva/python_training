import allure

from model.group import Group
import random


def test_edit_some_group(app, db, json_groups, check_ui):
    if len(db.get_groups_list()) == 0:
        app.group.create_group(Group(name="test"))
    with allure.step("Given a group list"):
        old_groups = db.get_groups_list()
    with allure.step("Given a selected group"):
        group = json_groups
        selected_group = random.choice(old_groups)
        group.id = selected_group.id
    with allure.step("When I edit the group"):
        app.group.edit_group_by_id(selected_group.id, group)
    with allure.step("Then the group list is equal to the old list with the edited group"):
        new_groups = db.get_groups_list()
        old_groups.remove(selected_group)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
