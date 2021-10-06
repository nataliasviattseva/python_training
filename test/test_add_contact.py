# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(
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
    app.logout()
