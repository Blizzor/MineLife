import json
import datetime
import logging
import mysql.connector

configs = {}

with open('config/config.json', "r") as json_file:
    jsonstructure = json.load(json_file)
    for p in jsonstructure['discord']:
        configs["token"] = p['token']
        configs["DBhost"] = p['DBhost']
        configs["DBuser"] = p['DBuser']
        configs["DBpasswd"] = p['DBpasswd']
        configs["DBdatabase"] = p['DBdatabase']
        configs["IDChannelSpawner"] = p['IDChannelSpawner']
        configs["IDEmote"] = p['IDEmote']
        configs["NameEmote"] = p['NameEmote']

with open("databaseConfig.json", "r") as json_file:
    dbConfig = json.load(json_file)

mydb = mysql.connector.connect(
    host=configs["DBhost"],
    user=configs["DBuser"],
    passwd=configs["DBpasswd"],
    database=configs["DBdatabase"],
    auth_plugin='mysql_native_password'
)
