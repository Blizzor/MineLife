import mysql.connector
import json
from modules import init

async def createOnLoad(db):
    if init.tables["createOnLoad"] == True:
        await createTables(db)

async def resetDatabase(db):

    try:
        cursor = db.cursor()

        await createTables(db, commit=False)

        for table in init.tables["tables"]:
            sql = f"DELETE FROM {table['name']}"
            cursor.execute(sql)

        for mob in init.mobs["mobs"]:
            sql = f"INSERT INTO {mob['database']['table']} ("
            columns = [column for column in mob['database']['defaultValues'].keys()]
            sql += ', '.join(columns)
            sql += ") VALUES ("
            sql += ', '.join(['%s' for column in columns])
            sql += ")"

            val = tuple([mob['database']['defaultValues'][column] for column in columns])
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
