def dict_fetch_all(cursor):
    """Return all rows from a cursor as a dict"""
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def dict_fetch_one(cursor):
    """Return one row from a cursor as a dict"""
    row = cursor.fetchone()
    if not row:
        return {}
    return dict(zip((col[0] for col in cursor.description), row))
