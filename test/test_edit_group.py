from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(
        name="editGroup",
        header="groupHeaderEdited",
        footer="groupFooterEdited"))
    app.session.logout()


def test_edit_name_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="editGroupSecondEdition"))
    app.session.logout()


def test_edit_header_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="groupHeaderSecondEdition"))
    app.session.logout()


def test_edit_footer_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="groupFooterSecondEdition"))
    app.session.logout()
