from model.entry import Entry


def test_add_entry(app, json_entries):
    entry = json_entries
    old_entries = app.entry.get_entries_list()
    app.entry.create_entry(entry)
    assert len(old_entries) + 1 == app.entry.count()
    new_entries = app.entry.get_entries_list()
    old_entries.append(entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
