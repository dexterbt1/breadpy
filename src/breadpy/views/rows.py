# -*- coding: utf-8 -*-
import breadpy.db as db
from breadpy.templates import get_template

def browse(table_name):
    """Show list of tables"""
    #template = get_template("tables/browse.html")
    #return template.render(list=list)
    return u"rows.browse %s" % table_name


