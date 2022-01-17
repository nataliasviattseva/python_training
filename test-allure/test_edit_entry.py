import allure

from model.entry import Entry
import random


def test_edit_some_entry(app, db, json_entries, check_ui):
    if len(db.get_entries_list()) == 0:
        app.entry.create_entry(Entry(first_name="test"))
    with allure.step("Given an entry list"):
        old_entries = db.get_entries_list()
    with allure.step("Given a selected entry"):
        entry = json_entries
        selected_entry = random.choice(old_entries)
        entry.id = selected_entry.id
    with allure.step("When I edit the entry"):
        app.entry.edit_entry_by_id(selected_entry.id, entry)
    with allure.step("Then the entry list is equal to the old list with the edited entry"):
        new_entries = db.get_entries_list()
        old_entries.remove(selected_entry)
        old_entries.append(entry)
        assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
