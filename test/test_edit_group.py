from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(
        name="editGroup",
        header="groupHeaderEdited",
        footer="groupFooterEdited"))


def test_edit_name_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(name="editGroupSecondEdition"))


def test_edit_header_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(header="groupHeaderSecondEdition"))


def test_edit_footer_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(footer="groupFooterSecondEdition"))
