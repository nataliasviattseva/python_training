from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    # assert lists of groups get from ui and db
    # ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    # db_list = map(clean, db.get_group_list())
    # assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

    # demonstration of loading speed from ui and db
    print(timeit(lambda: app.group.get_group_list(), number=1))
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False  # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
