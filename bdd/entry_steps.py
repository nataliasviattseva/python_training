from pytest_bdd import given, when, then
from model.entry import Entry
import random


@given("an entry list", target_fixture="entry_list")
def entry_list(db):
    return db.get_entries_list()


@given("an entry with <first_name> and <last_name>", target_fixture="new_entry")
def new_entry(first_name, last_name):
    return Entry(first_name=first_name, last_name=last_name)


@when("I add the entry to the list")
def add_new_entry(app, new_entry):
    app.entry.create_entry(new_entry)


@then("the new entry list is equal to the old list with the added entry")
def verify_entry_added(db, entry_list, new_entry):
    old_entries = entry_list
    new_entries = db.get_entries_list()
    old_entries.append(new_entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)


@given("an entry with <edit_first_name> and <edit_last_name>", target_fixture="edited_entry")
def edited_entry(edit_first_name, edit_last_name):
    return Entry(first_name=edit_first_name, last_name=edit_last_name)


@given("a selected entry", target_fixture="selected_entry")
def selected_entry(entry_list):
    return random.choice(entry_list)


@when("I edit the entry")
def edit_entry(app, selected_entry, edited_entry):
    edited_entry.id = selected_entry.id
    app.entry.edit_entry_by_id(selected_entry.id, edited_entry)


@then("the entry list is equal to the old list with the edited entry")
def verify_entry_edited(db, entry_list, selected_entry, edited_entry):
    old_entries = entry_list
    new_entries = db.get_entries_list()
    old_entries.remove(selected_entry)
    old_entries.append(edited_entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)


@when("I delete the entry")
def delete_entry(app, selected_entry):
    app.entry.delete_entry_by_id(selected_entry.id)


@then("the new entry list is equal to the old list with the deleted entry")
def verify_entry_deleted(db, entry_list, selected_entry):
    old_entries = entry_list
    new_entries = db.get_entries_list()
    old_entries.remove(selected_entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
