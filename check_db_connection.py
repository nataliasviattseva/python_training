import pymysql.cursors
from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    entries = db.get_entries_list()
    for entry in entries:
        print(entry)
    print(len(entries))
finally:
    db.destroy()
