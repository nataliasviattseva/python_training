from selenium.webdriver.support.ui import Select
from model.entry import Entry


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

    def edit_first_entry(self, new_entry_data):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_first_entry_for_edit()
        self.fill_entry_form(new_entry_data)
        self.perform_action("update")
        self.return_to_home_page()

    def select_first_entry_for_edit(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[title=\"Edit\"]").click()

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
        wd = self.app.wd
        self.return_to_home_page()
        self.select_first_entry()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def select_first_entry(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

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

    def get_entries_list(self):
        wd = self.app.wd
        self.return_to_home_page()
        entries = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']/td[@class='center']/input/../.."):
            entry_id = element.find_element_by_xpath("//input").get_attribute("value")
            cell1 = element.find_element_by_xpath("//td[2]").text
            cell2 = element.find_element_by_xpath("//td[3]").text
            entries.append(Entry(first_name=cell1, last_name=cell2, id=entry_id))
        return entries
