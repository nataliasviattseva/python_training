from model.entry import Entry
from random import randrange


def test_edit_some_entry(app, json_entries):
    if app.entry.count() == 0:
        app.entry.create_entry(Entry(first_name="test"))
    old_entries = app.entry.get_entries_list()
    index = randrange(len(old_entries))
    entry = json_entries
    entry.id = old_entries[index].id
    app.entry.edit_entry_by_index(index, entry)
    assert len(old_entries) == app.entry.count()
    new_entries = app.entry.get_entries_list()
    old_entries[index] = entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
