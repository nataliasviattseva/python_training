# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create_group(Group(name="newGroup", header="groupHeader", footer="groupFooter"))


def test_add_empty_group(app):
    app.group.create_group(Group(name="", header="", footer=""))
