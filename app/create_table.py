"""
Connect to oracle and create a table
"""

import getpass

import oracledb

un = 'sys'
cs = 'localhost:1521/FREE'
pw = getpass.getpass(f'Enter password for {un}@{cs}: ')

with oracledb.connect(user=un, password=pw, dsn=cs, mode=oracledb.SYSDBA) as connection:
    with connection.cursor() as cursor:
        sql = """
        CREATE TABLE IF NOT EXISTS member (
            id NUMBER,
            first_name VARCHAR2(200),
            last_name VARCHAR2(200),
            email VARCHAR2(200),
            gender VARCHAR2(50),
            location VARCHAR2(100),
            PRIMARY KEY (id)
        )
        """
        cursor.execute(sql)
        connection.commit()
        print("Done")
