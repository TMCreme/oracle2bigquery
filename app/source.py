"""
Connect to oracle
"""
import getpass
import oracledb

from app.main import add_data

un = 'sys'
cs = 'localhost:1521/FREE'
pw = getpass.getpass(f'Enter password for {un}@{cs}: ')

myoffset = 0
maxrows = 100


with oracledb.connect(
    user=un, password=pw, dsn=cs, mode=oracledb.SYSDBA
        ) as connection:
    with connection.cursor() as cursor:
        sql = """
            SELECT * FROM member
            OFFSET :offset ROWS FETCH NEXT :maxnumrows ROWS ONLY
        """
        for row in cursor.execute(sql, offset=myoffset, maxnumrows=maxrows):
            data_row = [
                {
                    "id": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "email": row[3],
                    "gender": row[4],
                    "location": row[5]
                }
            ]
            add_data(data_row)
