from pytest_bdd import scenario
from .entry_steps import *

@scenario('entries.feature', 'Add new entry')
def test_add_new_entry():
    pass

@scenario('entries.feature', 'Edit the entry')
def test_edit_entry():
    pass

@scenario('entries.feature', 'Delete the entry')
def test_delete_entry():
    pass