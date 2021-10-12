# -*- coding: utf-8 -*-
from model.entry import Contact


def test_add_entry(app):
    app.entry.create_entry(
        Contact(first_name="FirstName",
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
                ayear="2001"))


def test_add_empty_entry(app):
    app.entry.create_entry(
        Contact(first_name="",
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
                ayear="-"))
