from model.entry import Entry
from model.group import Group
import random


def test_add_entry_in_group(app, orm, db):
    if len(db.get_groups_without_entries()) == 0:
        app.group.create_group(Group(name="test_group"))

    if len(db.get_entries_not_in_any_group()) == 0:
        app.entry.create_entry(Entry(first_name="test_entry"))

    groups = db.get_groups_without_entries()
    selected_group = random.choice(groups)

    entries = db.get_entries_not_in_any_group()
    selected_entry = random.choice(entries)

    app.entry.add_entry_in_group(selected_entry.id, selected_group.id)

    entries_in_group = orm.get_entries_in_group(selected_group)

    assert selected_entry in entries_in_group


def test_delete_entry_from_group(app, orm, db, check_ui):
    if len(orm.get_groups_list()) == 0:
        initial_group = Group(name="test_group")
        app.group.create_group(initial_group)

    if len(orm.get_entries_list()) == 0:
        initial_entry = Entry(first_name="test_entry")
        app.entry.create_entry(initial_entry)
        app.entry.add_entry_in_group(initial_entry.id, initial_group.id)

    groups = orm.get_groups_list()
    selected_group = random.choice(groups)

    entries_in_selected_group = orm.get_entries_in_group(selected_group)

    if len(entries_in_selected_group) == 0:
        selected_entry = random.choice(orm.get_entries_list())
        app.entry.add_entry_in_group(selected_entry.id, selected_group.id)
        entries_in_selected_group = orm.get_entries_in_group(selected_group)

    selected_entry = random.choice(entries_in_selected_group)

    app.entry.delete_entry_from_group(selected_entry.id, selected_group.id)

    entries_in_group = orm.get_entries_in_group(selected_group)

    assert selected_entry not in entries_in_group
