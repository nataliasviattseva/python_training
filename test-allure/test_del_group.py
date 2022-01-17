import allure

from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_groups_list()) == 0:
        app.group.create_group(Group(name="test"))
    with allure.step("Given a group list"):
        old_groups = db.get_groups_list()
    with allure.step("Given a selected group"):
        group = random.choice(old_groups)
    with allure.step("When I delete the group"):
        app.group.delete_group_by_id(group.id)
    with allure.step("Then the new group list is equal to the old list with the deleted group"):
        new_groups = db.get_groups_list()
        old_groups.remove(group)
        assert old_groups == new_groups
