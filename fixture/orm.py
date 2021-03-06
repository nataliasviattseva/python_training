from pony.orm import *
from datetime import datetime
from model.group import Group
from model.entry import Entry


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        entries = Set(lambda: ORMFixture.ORMEntry,
                      table="address_in_groups",
                      column="id",
                      reverse="groups",
                      lazy=True)

    class ORMEntry(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup,
                     table="address_in_groups",
                     column="group_id",
                     reverse="entries",
                     lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, autocommit=True)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_entries_to_model(self, entries):
        def convert(entry):
            return Entry(id=str(entry.id), first_name=entry.firstname, last_name=entry.lastname)

        return list(map(convert, entries))

    @db_session
    def get_groups_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_entries_list(self):
        return self.convert_entries_to_model(select(e for e in ORMFixture.ORMEntry if e.deprecated is None))

    @db_session
    def get_entries_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_entries_to_model(orm_group.entries)

    @db_session
    def get_entries_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_entries_to_model(
            select(e for e in ORMFixture.ORMEntry if e.deprecated is None and orm_group not in e.groups))

    @db_session
    def get_groups_with_entry(self, entry):
        orm_entry = list(select(e for e in ORMFixture.ORMEntry if e.id == entry.id))[0]
        return self.convert_groups_to_model(orm_entry.groups)

    @db_session
    def get_groups_without_entries(self):
        orm_entry = list(select(e for e in ORMFixture.ORMEntry if e.id == entry.id))[0]
        return self.convert_groups_to_model(select(e for e in ORMFixture.ORMGroup if orm_entry not in e.entries))

    @db_session
    def get_entries_not_in_any_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_entries_to_model(
            select(e for e in ORMFixture.ORMContact if orm_group not in e.groups))

    @db_session
    def get_groups_without_entries(self, entry):
        orm_entry = list(select(e for e in ORMFixture.ORMEntry if e.id == entry.id))
        return self.convert_groups_to_model(
            select(g for g in ORMFixture.ORMGroupif if orm_entry not in g.entries))

