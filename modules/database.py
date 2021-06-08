import mysql.connector
import json

with open('config/config.json') as json_file:
    jsonstructure = json.load(json_file)
    for p in jsonstructure['discord']:
        DBhost = p['DBhost']
        DBuser = p['DBuser']
        DBpasswd = p['DBpasswd']
        DBdatabase = p['DBdatabase']

with open('databaseConfig.json') as dbConf_file:
    dbConfig = json.load(dbConf_file)

mydb = mysql.connector.connect(
    host=DBhost,
    user=DBuser,
    passwd=DBpasswd,
    database=DBdatabase,
    auth_plugin='mysql_native_password'
)

async def resetDatabase():

    cursor = mydb.cursor()

    for table in dbConfig["tables"]:
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

    
