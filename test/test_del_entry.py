

def test_delete_first_entry(app):
    app.session.login(username="admin", password="secret")
    app.entry.delete_first_entry()
    app.session.logout()
