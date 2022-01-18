import json
import os.path
from fixture.application import Application
from fixture.db import DbFixture
from model.group import Group
from model.entry import Entry


class AddressBook:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="firefox"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config['baseUrl'])
        self.fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
        db_config = self.target['db']
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                                   password=db_config['password'])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_groups_list(self):
        return self.dbfixture.get_groups_list()

    def create_group(self, group):
        self.fixture.group.create_group(group)

    def edit_group(self, group, new_group):
        self.fixture.group.edit_group_by_id(group.id, new_group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def new_entry(self, first_name, last_name):
        return Entry(first_name=first_name, last_name=last_name)

    def get_entries_list(self):
        return self.dbfixture.get_entries_list()

    def create_entry(self, entry):
        self.fixture.entry.create_entry(entry)

    def edit_entry(self, entry, new_entry):
        self.fixture.entry.edit_entry_by_id(entry.id, new_entry)

    def delete_entry(self, entry):
        self.fixture.entry.delete_entry_by_id(entry.id)
