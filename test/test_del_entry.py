from model.entry import Entry
import random
import time


def test_delete_some_entry(app, db, check_ui):
    if len(db.get_entries_list()) == 0:
        app.entry.create_entry(Entry(first_name="test"))
    old_entries = db.get_entries_list()
    entry = random.choice(old_entries)
    app.entry.delete_entry_by_id(entry.id)
    new_entries = db.get_entries_list()
    assert len(old_entries) - 1 == len(new_entries)
    old_entries.remove(entry)
    assert old_entries == new_entries
    if check_ui:
        assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_entries_list(), key=Entry.id_or_max)
