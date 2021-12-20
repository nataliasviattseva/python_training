from model.entry import Entry
from model.group import Group
import random


def test_add_entry_in_group(app, orm, db, json_entries, json_groups, check_ui):
    if len(orm.get_groups_list()) == 0:
        app.group.create_group(Group(name="test_group"))

    if len(orm.get_entries_list()) == 0:
        app.entry.create_entry(Entry(first_name="test_entry"))

    entries = db.get_entries_list()
    entry = json_entries
    selected_entry = random.choice(entries)
    entry.id = selected_entry.id

    # group_without_entries = orm.get_groups_without_entries(selected_entry)

    groups = orm.get_groups_list()
    group = json_groups
    selected_group = random.choice(groups)
    group.id = selected_group.id

    app.entry.add_entry_in_group(entry.id, group.id)

    entries_in_group = orm.get_entries_in_group(group)

    assert selected_entry in entries_in_group

    # new_entries = db.get_entries_list()

    # assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
    # if check_ui:
    #     assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_groups_list(), key=Entry.id_or_max)

# def test_delete_entry_from_group(app, db, check_ui):
#     if len(db.get_entries_list()) == 0:
#         app.entry.create_entry(Entry(first_name="test"))
#     old_entries = db.get_entries_list()
#     entry = random.choice(old_entries)
#     app.entry.delete_entry_by_id(entry.id)
#     new_entries = db.get_entries_list()
#     old_entries.remove(entry)
#     assert old_entries == new_entries
#     if check_ui:
#         assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_group_list(), key=Entry.id_or_max)
