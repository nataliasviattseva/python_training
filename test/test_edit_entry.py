from model.entry import Entry
from random import randrange


def test_edit_some_entry(app, db, json_entries, check_ui):
    if len(db.get_entries_list()) == 0:
        app.entry.create_entry(Entry(first_name="test"))
    old_entries = db.get_entries_list()
    index = randrange(len(old_entries))
    entry = json_entries
    entry.id = old_entries[index].id
    app.entry.edit_entry_by_index(index, entry)
    assert len(old_entries) == app.entry.count()
    new_entries = db.get_entries_list()
    old_entries[index] = entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
    if check_ui:
        assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_group_list(), key=Entry.id_or_max)
