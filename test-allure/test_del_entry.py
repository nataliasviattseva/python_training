import allure

from model.entry import Entry
import random


def test_delete_some_entry(app, db, check_ui):
    if len(db.get_entries_list()) == 0:
        app.entry.create_entry(Entry(first_name="test"))
    with allure.step("Given an entry list"):
        old_entries = db.get_entries_list()
    with allure.step("Given a selected entry"):
        entry = random.choice(old_entries)
    with allure.step("When I delete the entry"):
        app.entry.delete_entry_by_id(entry.id)
    with allure.step("Then the new entry list is equal to the old list with the deleted entry"):
        new_entries = db.get_entries_list()
        assert len(old_entries) - 1 == len(new_entries)
        old_entries.remove(entry)
        assert old_entries == new_entries
