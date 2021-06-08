import mysql.connector
import json
from modules import init

async def resetDatabase(db):

    try:
        cursor = db.cursor()

        for table in init.dbConfig["tables"]:
            sql = f"CREATE TABLE {table['name']} ("
            sql += ', '.join(f"{column['name']} {column['type']} {column['additional']}" for column in table["columns"])
            sql += ')'

            cursor.execute(sql)

            for defaults in table["defaultValues"]:
                sql = f"INSERT INTO {table["name"]} ("
                columns = [column["name"] for column in table["columns"]]
                sql += ', '.join(columns)
                sql += ") VALUES ("
                sql += ', '.join(['?' for column in columns])
                sql += ")"

        db.commit()
    except:
        db.rollback()
