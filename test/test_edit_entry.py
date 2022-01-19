from model.entry imsorted(old_entries, key=Entry.id_or_max)port Entry
import random


def test_edit_some_entry(app, db, json_entries, check_ui):
    if len(db.get_entries_list()) == 0:
        app.entry.create_entry(Entry(first_name="test"))
    old_entries = db.get_entries_list()
    entry = json_entries
    selected_entry = random.choice(old_entries)
    entry.id = selected_entry.id
    app.entry.edit_entry_by_id(selected_entry.id, entry)
    new_entries = db.get_entries_list()
    old_entries.remove(selected_entry)
    old_entries.append(entry)
    assert  == sorted(new_entries, key=Entry.id_or_max)
    if check_ui:
        assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_entries_list(), key=Entry.id_or_max)
