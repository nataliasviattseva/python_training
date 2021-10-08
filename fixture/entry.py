from selenium.webdriver.support.ui import Select

class EntryHelper:

    def __init__(self, app):
        self.app = app

    def create_entry(self, entry):
        wd = self.app.wd
        # init entry creation
        wd.find_element_by_link_text("add new").click()
        self.fill_entry_form(entry, wd)
        # submit entry creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def edit_first_entry(self, entry):
        wd = self.app.wd
        self.return_to_home_page()
        # select first entry
        wd.find_element_by_css_selector("img[title=\"Edit\"]").click()
        self.fill_entry_form(entry, wd)
        # submit entry creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def fill_entry_form(self, entry, wd):
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(entry.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(entry.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(entry.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(entry.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(entry.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(entry.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(entry.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(entry.phone_home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(entry.phone_mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(entry.phone_work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(entry.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(entry.email1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(entry.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(entry.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(entry.homepage)
        # enter birthday
        Select(wd.find_element_by_name("bday")).select_by_visible_text(entry.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(entry.bmonth)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(entry.byear)
        # enter anniversary
        Select(wd.find_element_by_name("aday")).select_by_visible_text(entry.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(entry.amonth)
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(entry.ayear)
        # enter secondary information
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(entry.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(entry.phone2_home)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(entry.notes)

    def delete_first_entry(self):
        wd = self.app.wd
        self.return_to_home_page()
        # select first entry
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()