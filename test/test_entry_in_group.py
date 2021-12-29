from model.entry import Entry
from model.group import Group
import random


def test_add_entry_in_group(app, orm,
                            db, json_entries, json_groups, check_ui):
    if len(db.get_groups_without_entries()) == 0:
        app.group.create_group(Group(name="test_group"))

    if len(db.get_entries_not_in_any_group()) == 0:
        app.entry.create_entry(Entry(first_name="test_entry"))

    groups = db.get_groups_without_entries()
    group = json_groups
    selected_group = random.choice(groups)
    group.id = selected_group.id

    entries = db.get_entries_not_in_any_group()
    entry = json_entries
    selected_entry = random.choice(entries)
    entry.id = selected_entry.id

    groups_without_selected_entry_before_add_entry = orm.get_groups_without_entry(selected_entry)

    app.entry.add_entry_in_group(selected_entry.id, selected_group.id)

    groups_without_selected_entry_after_add_entry = orm.get_groups_without_entry(selected_entry)

    entries_in_group = orm.get_entries_in_group(group)

    assert len(groups_without_selected_entry_after_add_entry) == len(groups_without_selected_entry_before_add_entry) - 1
    assert selected_entry in entries_in_group


def test_delete_entry_from_group(app, orm, db, json_entries, json_groups, check_ui):
    if len(orm.get_groups_list()) == 0:
        initial_group = Group(name="test_group")
        app.group.create_group(initial_group)

    if len(orm.get_entries_list()) == 0:
        initial_entry = Entry(first_name="test_entry")
        app.entry.create_entry(initial_entry)
        app.entry.add_entry_in_group(initial_entry.id, initial_group.id)

    groups = orm.get_groups_list()
    group = json_groups
    selected_group = random.choice(groups)
    group.id = selected_group.id

    entries_in_selected_group = orm.get_entries_in_group(selected_group)
    entry = json_entries

    if len(entries_in_selected_group) == 0:
        selected_entry = random.choice(orm.get_entries_list())
        app.entry.add_entry_in_group(selected_entry.id, selected_group.id)
        entries_in_selected_group = orm.get_entries_in_group(selected_group)

    selected_entry = random.choice(entries_in_selected_group)
    entry.id = selected_entry.id

    groups_without_selected_entry_before_delete_entry = orm.get_groups_without_entry(selected_entry)

    app.entry.delete_entry_from_group(entry.id, group.id)

    entries_in_group = orm.get_entries_in_group(group)

    groups_without_selected_entry_after_delete_entry = orm.get_groups_without_entry(selected_entry)

    assert len(groups_without_selected_entry_after_delete_entry) == len(groups_without_selected_entry_before_delete_entry) + 1
    assert selected_entry not in entries_in_group
