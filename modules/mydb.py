import mysql.connector
import json

with open('config/config.json') as json_file:
    jsonstructure = json.load(json_file)
    for p in jsonstructure['discord']:
        DBhost = p['DBhost']
        DBuser = p['DBuser']
        DBpasswd = p['DBpasswd']
        DBdatabase = p['DBdatabase']

mydb = mysql.connector.connect(
    host=DBhost,
    user=DBuser,
    passwd=DBpasswd,
    database=DBdatabase,
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE mobs")

#create table
mycursor.execute("CREATE TABLE mobs (id INT AUTO_INCREMENT PRIMARY KEY,name TINYTEXT,hp DOUBLE, hpfactor DOUBLE, dmg DOUBLE, dmgfactor DOUBLE, def DOUBLE, deffactor DOUBLE, evasion DOUBLE, evasionfactor DOUBLE, aim DOUBLE, aimfactor DOUBLE, xp DOUBLE, xpfactor DOUBLE)")

sql = "INSERT INTO mobs (name, hp, hpfactor, dmg, dmgfactor, def, deffactor, evasion, evasionfactor, aim, aimfactor, xp, xpfactor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = ("Zombie", 20.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 5.0, 1.1)

mycursor.execute(sql, val)
#mydb.commit()

val = ("Creeper", 18.0, 1.1, 3.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 5.0, 1.1)

mycursor.execute(sql, val)
#mydb.commit()

val = ("Skeleton", 20.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 5.0, 1.1)

mycursor.execute(sql, val)

val = ("Enderman", 30.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 10.0, 1.1)

mycursor.execute(sql, val)
mydb.commit()