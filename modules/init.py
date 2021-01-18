import json
import datetime
import logging
import mysql.connector

class config():
    def __init__(self):
        with open('config/config.json') as json_file:
            jsonstructure = json.load(json_file)
            for p in jsonstructure['discord']:
                self.token = p['token']
                self.DBhost = p['DBhost']
                self.DBuser = p['DBuser']
                self.DBpasswd = p['DBpasswd']
                self.DBdatabase = p['DBdatabase']
                self.IDChannelSpawner = p['IDChannelSpawner']
                self.IDEmote = p['IDEmote']
                self.NameEmote = p['NameEmote']

    def get_token(self):
        return self.token
    def get_DBhost(self):
        return self.DBhost
    def get_DBuser(self):
        return self.DBuser
    def get_DBpasswd(self):
        return self.DBpasswd
    def get_DBdatabase(self):
        return self.DBdatabase
    def get_IDChannelSpawner(self):
        return self.IDChannelSpawner
    def get_IDEmote(self):
        return self.IDEmote
    def get_NameEmote(self):
        return self.NameEmote

mydb = mysql.connector.connect(
    host=config().get_DBhost(),
    user=config().get_DBuser(),
    passwd=config().get_DBpasswd(),
    database=config().get_DBdatabase(),
    auth_plugin='mysql_native_password'
)

def getdb():
    return(mydb)
