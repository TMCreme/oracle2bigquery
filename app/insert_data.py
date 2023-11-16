"""
Connect to oracle and insert data
"""
import csv
import getpass
import oracledb

un = 'sys'
cs = 'localhost:1521/FREE'
pw = getpass.getpass(f'Enter password for {un}@{cs}: ')

with oracledb.connect(user=un, password=pw, dsn=cs, mode=oracledb.SYSDBA) as connection:
    with connection.cursor() as cursor:
        with open("MOCK_DATA.csv") as csv_file:
            content = csv.reader(csv_file, delimiter=",")
            for row in content:
                sql = """
                    INSERT INTO member (
                    id, first_name, last_name, email, gender, location
                    ) VALUES (
                    :id, :first_name, :last_name, :email, :gender, :location
                    )
                """
                vals = (int(row[0]), row[1], row[2], row[3], row[4], row[5])
                cursor.execute(
                    sql, vals
                    )
        connection.commit()
        print("Done")
