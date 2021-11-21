from model.entry import Entry
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of entries", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 7
f = "data/entries.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10 + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits + " " * 10 + "(" * 10 + ")" * 10 + "-" * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen1, maxlen2, maxlen3):
    symbols = string.ascii_letters + string.digits + "."
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen1))]) + \
           "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen2))]) + \
           "." + "".join([random.choice(symbols) for i in range(random.randrange(maxlen3))])


testdata = [Entry(first_name="",
                  middle_name="",
                  last_name="",
                  nickname="",
                  title="",
                  company="",
                  address="",
                  phone_home="",
                  phone_mobile="",
                  phone_work="",
                  fax="",
                  email1="",
                  email2="",
                  email3="",
                  homepage="",
                  address2="",
                  phone2_home="",
                  notes="",
                  bday="",
                  bmonth="-",
                  byear="-",
                  aday="",
                  amonth="-",
                  ayear="-")
            ] + [Entry(first_name=random_string("FirstName", 10),
                       middle_name=random_string("MiddleName", 10),
                       last_name=random_string("LastName", 10),
                       nickname=random_string("nickname", 5),
                       title=random_string("Mr.", 1),
                       company=random_string("noname", 10),
                       address=random_string("123 address", 50),
                       phone_home=random_phone(10),
                       phone_mobile=random_phone(10),
                       phone_work=random_phone(10),
                       fax=random_phone(10),
                       email1=random_email(10, 10, 3),
                       email2=random_email(10, 10, 3),
                       email3=random_email(10, 10, 3),
                       homepage="www.homepage.com",
                       address2=random_string("456 address", 50),
                       phone2_home=random_phone(10),
                       notes=random_string("notes", 50),
                       bday="1",
                       bmonth="January",
                       byear="2000",
                       aday="5",
                       amonth="February",
                       ayear="2001")
                 for i in range(5)
                 ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
