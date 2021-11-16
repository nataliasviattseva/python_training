from selenium.webdriver.support.ui import Select
from model.entry import Entry
import re


class EntryHelper:

    def __init__(self, app):
        self.app = app

    def create_entry(self, entry_data):
        wd = self.app.wd
        # init entry creation
        wd.find_element_by_link_text("add new").click()
        self.fill_entry_form(entry_data)
        # submit entry creation
        self.perform_action("submit")
        self.return_to_home_page()
        self.entry_cache = None

    def edit_first_entry(self, new_entry_data):
        self.edit_entry_by_index(0)

    def edit_entry_by_index(self, index, new_entry_data):
        self.return_to_home_page()
        self.select_entry_by_index_for_edit(index)
        self.fill_entry_form(new_entry_data)
        self.perform_action("update")
        self.return_to_home_page()
        self.entry_cache = None

    def select_first_entry_for_edit(self):
        self.select_entry_by_index_for_edit(0)

    def select_entry_by_index_for_edit(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def select_entry_by_index_for_view(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def fill_entry_form(self, entry):
        self.change_field_value("firstname", entry.first_name)
        self.change_field_value("middlename", entry.middle_name)
        self.change_field_value("lastname", entry.last_name)
        self.change_field_value("nickname", entry.nickname)
        self.change_field_value("title", entry.title)
        self.change_field_value("company", entry.company)
        self.change_field_value("address", entry.address)
        self.change_field_value("home", entry.phone_home)
        self.change_field_value("mobile", entry.phone_mobile)
        self.change_field_value("work", entry.phone_work)
        self.change_field_value("fax", entry.fax)
        self.change_field_value("email", entry.email1)
        self.change_field_value("email2", entry.email2)
        self.change_field_value("email3", entry.email3)
        self.change_field_value("homepage", entry.homepage)
        # enter birthday
        self.change_select_value("bday", entry.bday)
        self.change_select_value("bmonth", entry.bmonth)
        self.change_field_value("byear", entry.byear)
        # enter anniversary
        self.change_select_value("aday", entry.aday)
        self.change_select_value("amonth", entry.amonth)
        self.change_field_value("ayear", entry.ayear)
        # enter secondary information
        self.change_field_value("address2", entry.address2)
        self.change_field_value("phone2", entry.phone2_home)
        self.change_field_value("notes", entry.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def delete_first_entry(self):
        self.delete_entry_by_index(0)

    def delete_entry_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_entry_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.entry_cache = None

    def select_first_entry(self):
        self.delete_entry_by_index(0)

    def select_entry_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def perform_action(self, action):
        wd = self.app.wd
        wd.find_element_by_name(action).click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    entry_cache = None

    def get_entries_list(self):
        if self.entry_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.entry_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                entry_id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                first_name = cells[2].text
                last_name = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.entry_cache.append(Entry(first_name=first_name,
                                              last_name=last_name,
                                              id=entry_id,
                                              address=address,
                                              all_emails_from_home_page=all_emails,
                                              all_phones_from_home_page=all_phones))
        return list(self.entry_cache)

    def get_entry_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_entry_by_index_for_edit(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        phone2_home = wd.find_element_by_name("phone2").get_attribute("value")
        return Entry(first_name=first_name,
                     last_name=last_name,
                     id=id,
                     address=address,
                     email1=email1,
                     email2=email2,
                     email3=email3,
                     phone_home=phone_home,
                     phone_mobile=phone_mobile,
                     phone_work=phone_work,
                     phone2_home=phone2_home)

    def get_entry_info_from_view_page(self, index):
        wd = self.app.wd
        self.select_entry_by_index_for_view(index)
        text = wd.find_element_by_id("content").text
        phone_home = re.search("H: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        phone2_home = re.search("P: (.*)", text).group(1)
        return Entry(phone_home=phone_home,
                     phone_mobile=phone_mobile,
                     phone_work=phone_work,
                     phone2_home=phone2_home)
