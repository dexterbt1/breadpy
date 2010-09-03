# -*- coding: utf-8 -*-
import breadpy.db as db
from breadpy.templates import get_template

def browse():
    """Show list of tables"""
    template = get_template("tables/browse.html")
    list = db.inspector.get_table_names()
    return template.render(list=list)

