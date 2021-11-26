from model.entry import Entry


def test_add_entry(app, db, json_entries, check_ui):
    entry = json_entries
    old_entries = db.get_entries_list()
    app.entry.create_entry(entry)
    new_entries = db.get_entries_list()
    old_entries.append(entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
    if check_ui:
        assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_group_list(), key=Entry.id_or_max)
