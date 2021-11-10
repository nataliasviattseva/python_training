import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.entry.get_entries_list()[0]
    contact_from_edit_page = app.entry.get_entry_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_pages(app):
    contact_from_view_page = app.entry.get_entry_info_from_view_page(0)
    contact_from_edit_page = app.entry.get_entry_info_from_edit_page(0)
    assert contact_from_view_page.phone_home == contact_from_edit_page.phone_home
    assert contact_from_view_page.phone_mobile == contact_from_edit_page.phone_mobile
    assert contact_from_view_page.phone_work == contact_from_edit_page.phone_work
    assert contact_from_view_page.phone2_home == contact_from_edit_page.phone2_home


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(entry):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [entry.phone_home, entry.phone_mobile, entry.phone_work, entry.phone2_home]))))
