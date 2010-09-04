# -*- coding: utf-8 -*-
import breadpy.db as db
from breadpy.templates import get_template
from sqlalchemy.engine import reflection

def browse():
    """ Show list of tables """
    template = get_template("tables/browse.html")
    inspector = reflection.Inspector.from_engine(db.engine)
    list = inspector.get_table_names()
    return template.render(list=list)

