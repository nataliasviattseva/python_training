from sys import maxsize


class Entry:

    def __init__(self,
                 first_name=None,
                 middle_name=None,
                 last_name=None,
                 nickname=None,
                 title=None,
                 company=None,
                 address=None,
                 phone_home=None,
                 phone_mobile=None,
                 phone_work=None,
                 fax=None,
                 email1=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 address2=None,
                 phone2_home=None,
                 notes=None,
                 bday=None,
                 bmonth=None,
                 byear=None,
                 aday=None,
                 amonth=None,
                 ayear=None,
                 id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2_home = phone2_home
        self.notes = notes
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
