# -*- coding: utf-8 -*-
import breadpy.db as db
from breadpy.templates import get_template
from sqlalchemy import MetaData, Table

def browse(table_name):
    """ Show list of rows of the given table_name"""
    # query
    meta = MetaData()
    table = Table(table_name, meta, autoload=True, autoload_with=db.engine)
    result = db.engine.execute(table.select())
    rows = result.fetchall()

    template = get_template("rows/browse.html")
    return template.render(table=table, rows=rows)


