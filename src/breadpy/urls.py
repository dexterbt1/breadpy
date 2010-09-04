urls = (
    # (route_uid, path, function)
    ("tables_browse", "/", "breadpy.views.tables.browse"),
    ("rows_browse", "/table/:table_name", "breadpy.views.rows.browse"),
)


