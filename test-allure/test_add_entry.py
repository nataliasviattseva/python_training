import allure

from model.entry import Entry


def test_add_entry(app, db, json_entries, check_ui):
    entry = json_entries
    with allure.step("Given an entry list"):
        old_entries = db.get_entries_list()
    with allure.step("When I add the entry to the list"):
        entry_id = app.entry.create_entry(entry)
    with allure.step("Then the new entry list is equal to the old list with the added entry"):
        entry.id = entry_id
        new_entries = db.get_entries_list()
        old_entries.append(entry)
        assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
