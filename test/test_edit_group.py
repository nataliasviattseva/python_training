from model.group import Group
import random


def test_edit_some_group(app, db, json_groups, check_ui):
    if len(db.get_groups_list()) == 0:
        app.group.create_group(Group(name="test"))
    old_groups = db.get_groups_list()
    group = json_groups
    selected_group = random.choice(old_groups)
    group.id = selected_group.id
    app.group.edit_group_by_id(selected_group.id, group)
    new_groups = db.get_groups_list()
    old_groups.remove(selected_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
