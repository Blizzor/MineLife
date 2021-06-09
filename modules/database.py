import mysql.connector
import json
from modules import init

async def createOnLoad(db):
    if init.tables["createOnLoad"] == True:
        createTables(db)

async def resetDatabase(db):

    try:
        cursor = db.cursor()

        createTables(db, commit=False)

        for table in init.tables["tables"]:
            for defaults in table["defaultValues"]:
                sql = f"INSERT INTO {table["name"]} ("
                columns = [column["name"] for column in table["columns"]]
                sql += ', '.join(columns)
                sql += ") VALUES ("
                sql += ', '.join(['%s' for column in columns])
                sql += ")"

                val = tuple([defaults[columnName] for columnName in columns])
                cursor.execute(sql,val)

        db.commit()
    except:
        db.rollback()

async def createTables(db, commit=True):
    try:
        cursor = db.cursor()

        for table in init.tables["tables"]:
            sql = f"CREATE TABLE {table['name']} ("
            sql += ', '.join(f"{column['name']} {column['type']} {column['additional']}" for column in table["columns"])
            sql += ')'

        cursor.execute(sql)

        if commit:
            db.commit()

    except:
        if commit:
            db.rollback()
