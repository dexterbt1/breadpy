# -*- coding: utf-8 -*-
import breadpy.settings as settings
import breadpy.db as db
from breadpy.templates import get_template
from sqlalchemy import MetaData, Table
from sqlalchemy.sql import select

def browse(table_name):
    """ Show list of rows of the given table_name """
    meta = MetaData()
    meta.reflect(db.engine)
    #table = Table(table_name, meta, autoload=True, autoload_with=db.engine)
    table = meta.tables[table_name]

    # setup query
    q_from = table
    columns = [ ]

    for tc in table.c.keys():
        q_c = table.c.get(tc)
        columns.append(q_c)
        if hasattr(settings, 'DISPLAY_FK'):
            # check if we need to join other tables
            try:
                join = set()
                fks = settings.DISPLAY_FK[table_name][tc]
                for fk in fks:
                    fktablename, fkcolname = fk.split(".", 2)
                    fktable = meta.tables[fktablename]
                    join.add(fktable)
                    fkcol = getattr(fktable.c, fkcolname)
                    fkcol.breadpy_fk = True
                    columns.append(fkcol)
                for jt in join:
                    q_from = q_from.join(jt)
            except KeyError, ke:
                pass
                
    q = select(from_obj=q_from, columns=columns)
    sql = "%s" % q

    # execute and fetch
    result = db.engine.execute(q)
    raw_rows = result.fetchall()
    rows = raw_rows

    template = get_template("rows/browse.html")

    return template.render(table=table, rows=rows, columns=columns, sql=sql)


