import pymysql.cursors
# import mysql.connector
from model.group import Group
from model.entry import Entry


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)
        # self.connection.autocommit = True # doesn't work, autocommit works only as an option above

    def get_groups_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer  from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_entries_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, "
                           "firstname, "
                           "middlename, "
                           "lastname, "
                           "nickname, "
                           "company, "
                           "title, "
                           "address, "
                           "home, "
                           "mobile, "
                           "work, "
                           "fax, "
                           "email, "
                           "email2, "
                           "email3, "
                           "homepage, "
                           "bday, "
                           "bmonth, "
                           "byear, "
                           "aday, "
                           "amonth, "
                           "ayear, "
                           "address2, "
                           "phone2, "
                           "notes "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address,
                 home, mobile, work, fax, email, email2, email3, homepage, bday, bmonth,
                 byear, aday, amonth, ayear, address2, phone2, notes) = row
                list.append(Entry(id=str(id),
                                  first_name=firstname,
                                  middle_name=middlename,
                                  last_name=lastname,
                                  nickname=nickname,
                                  company=company,
                                  title=title,
                                  address=address,
                                  phone_home=home,
                                  phone_mobile=mobile,
                                  phone_work=work,
                                  fax=fax,
                                  email1=email,
                                  email2=email2,
                                  email3=email3,
                                  homepage=homepage,
                                  bday=bday,
                                  bmonth=bmonth,
                                  byear=byear,
                                  aday=aday,
                                  amonth=amonth,
                                  ayear=ayear,
                                  address2=address2,
                                  phone2_home=phone2,
                                  notes=notes))
        finally:
            cursor.close()
        return list

    def get_groups_without_entries(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list "
                           "where group_id not in (select group_id from address_in_groups)")
            for row in cursor:
                (id, name) = row
                list.append(Group(id=str(id), name=name))
        finally:
            cursor.close()
        return list

    def get_entries_not_in_any_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook "
                           "where id not in (select id from address_in_groups)")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Entry(id=str(id), first_name=firstname, last_name=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
