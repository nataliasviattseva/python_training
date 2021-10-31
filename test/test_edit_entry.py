# -*- coding: utf-8 -*-
from model.entry import Entry


def test_edit_first_entry(app):
    if app.entry.count() == 0:
        app.entry.create_entry(Entry(first_name="test"))
    old_entries = app.entry.get_entries_list()
    entry = Entry(first_name="FirstNameEdited",
              middle_name="MiddleNameEdited",
              last_name="LastNameEdited",
              nickname="nicknameEdited",
              title="Mr.Edited",
              company="nonameEdited",
              address="1234 Address line 1 Edited\nAddress line 2 Edited",
              phone_home="12345678 Edited",
              phone_mobile="23456789 Edited",
              phone_work="34567890 Edited",
              fax="45678901 Edited",
              email1="email1Edited@mail.com",
              email2="email2Edited@mail.com",
              email3="email2Edited@mail.com",
              homepage="www.homepageEdited.com",
              address2="123 Secondary Address line 1 Edited\nSecondary Address line 2 Edited",
              phone2_home="homeEdited",
              notes="notesEdited",
              bday="2",
              bmonth="February",
              byear="2001",
              aday="6",
              amonth="March",
              ayear="2002")
    entry.id = old_entries[0].id
    app.entry.edit_first_entry(entry)
    assert len(old_entries) == app.entry.count()
    new_entries = app.entry.get_entries_list()
    old_entries[0] = entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
