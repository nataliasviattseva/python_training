import re


# check one entry from home page and edit page
# def test_contact_on_home_page(app):
#     contact_from_home_page = app.entry.get_entries_list()[0]
#     contact_from_edit_page = app.entry.get_entry_info_from_edit_page(0)
#     assert contact_from_home_page.last_name == contact_from_edit_page.last_name
#     assert contact_from_home_page.first_name == contact_from_edit_page.first_name
#     assert contact_from_home_page.address == contact_from_edit_page.address
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_check_contact_on_home_page_with_contacts_from_db(app, db):
    contact_from_home_page = app.entry.get_entries_list()
    contact_from_db = db.get_entries_list()
    list = {}
    for entry in contact_from_home_page:
        list.setdefault(entry.id, entry)
    for entry in contact_from_db:
        contact_from_home_page = list[entry.id]
        assert contact_from_home_page.last_name == entry.last_name.rstrip()
        assert contact_from_home_page.first_name == entry.first_name
        assert clear(contact_from_home_page.address) == clear(entry.address)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(entry)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(entry)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(entry):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [entry.phone_home, entry.phone_mobile, entry.phone_work, entry.phone2_home]))))


def merge_emails_like_on_home_page(entry):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [entry.email1, entry.email2, entry.email3])))
