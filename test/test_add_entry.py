# -*- coding: utf-8 -*-
from model.entry import Entry


def test_add_entry(app):
      old_entries = app.entry.get_entries_list()
      entry = Entry(first_name="FirstName",
                    middle_name="MiddleName",
                    last_name="LastName",
                    nickname="nickname",
                    title="Mr.",
                    company="noname",
                    address="1234 Address line 1\nAddress line 2",
                    phone_home="12345678",
                    phone_mobile="23456789",
                    phone_work="34567890",
                    fax="45678901",
                    email1="email1@mail.com",
                    email2="email2@mail.com",
                    email3="email2@mail.com",
                    homepage="www.homepage.com",
                    address2="123 Secondary Address line 1\nSecondary Address line 2",
                    phone2_home="home",
                    notes="notes",
                    bday="1",
                    bmonth="January",
                    byear="2000",
                    aday="5",
                    amonth="February",
                    ayear="2001")
      app.entry.create_entry(entry)
      assert len(old_entries) + 1 == app.entry.count()
      new_entries = app.entry.get_entries_list()
      old_entries.append(entry)
      assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)


def test_add_empty_entry(app):
      old_entries = app.entry.get_entries_list()
      entry = Entry(first_name="",
                    middle_name="",
                    last_name="",
                    nickname="",
                    title="",
                    company="",
                    address="",
                    phone_home="",
                    phone_mobile="",
                    phone_work="",
                    fax="",
                    email1="",
                    email2="",
                    email3="",
                    homepage="",
                    address2="",
                    phone2_home="",
                    notes="",
                    bday="",
                    bmonth="-",
                    byear="-",
                    aday="",
                    amonth="-",
                    ayear="-")
      app.entry.create_entry(entry)
      assert len(old_entries) + 1 == app.entry.count()
      new_entries = app.entry.get_entries_list()
      old_entries.append(entry)
      assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)

def test_add_entry_with_main_info(app):
      old_entries = app.entry.get_entries_list()
      entry = Entry(first_name="Ivanov",
                    middle_name="",
                    last_name="Ivan",
                    nickname="",
                    title="",
                    company="",
                    address="44 Allee de la Rue",
                    phone_home="07.77.77.77.77",
                    phone_mobile="",
                    phone_work="",
                    fax="",
                    email1="",
                    email2="",
                    email3="",
                    homepage="",
                    address2="",
                    phone2_home="",
                    notes="",
                    bday="3",
                    bmonth="April",
                    byear="2000",
                    aday="",
                    amonth="-",
                    ayear="-")
      app.entry.create_entry(entry)
      assert len(old_entries) + 1 == app.entry.count()
      new_entries = app.entry.get_entries_list()
      old_entries.append(entry)
      assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
