import allure

from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step("Given a group list"):
        old_groups = db.get_groups_list()
    with allure.step("When I add the group to the list"):
        app.group.create_group(group)
    with allure.step("Then the new group list is equal to the old list with the added group"):
        new_groups = db.get_groups_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
