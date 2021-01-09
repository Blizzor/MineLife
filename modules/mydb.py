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
async def installdb():

    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE mobs")
    #mycursor.execute("DROP TABLE players")
    #mycursor.execute("DROP TABLE items")
    #mycursor.execute("DROP TABLE weapon")
    #mycursor.execute("DROP TABLE bow")
    #mycursor.execute("DROP TABLE shield")
    #mycursor.execute("DROP TABLE armor")

    #mycursor.execute("DROP TABLE playeritems")

    #create table
    mycursor.execute("CREATE TABLE mobs (id INT AUTO_INCREMENT PRIMARY KEY,name TINYTEXT,hp DOUBLE, hpfactor DOUBLE, dmg DOUBLE, dmgfactor DOUBLE, def DOUBLE, deffactor DOUBLE, evasion DOUBLE, evasionfactor DOUBLE, aim DOUBLE, aimfactor DOUBLE, xp DOUBLE, xpfactor DOUBLE)")
    #mycursor.execute("CREATE TABLE players (id INT AUTO_INCREMENT PRIMARY KEY, discord_id INT, name TINYTEXT,level INT, fullhp DOUBLE,hp DOUBLE, dmg DOUBLE, def DOUBLE, evasion DOUBLE, aim DOUBLE, xp DOUBLE, mainweapon INT, mainarmor INT, mainpotion INT)")
    #mycursor.execute("CREATE TABLE items (id INT AUTO_INCREMENT PRIMARY KEY, minecraft_id INT, name TINYTEXT,food BOOL, potion BOOL)")
    #mycursor.execute("CREATE TABLE weapon (id INT AUTO_INCREMENT PRIMARY KEY, discord_id INT, name TINYTEXT, dmg DOUBLE, aimfactor DOUBLE)")
    #mycursor.execute("CREATE TABLE bow (id INT AUTO_INCREMENT PRIMARY KEY, discord_id INT, name TINYTEXT, dmg DOUBLE, aimfactor DOUBLE)")
    #mycursor.execute("CREATE TABLE shield (id INT AUTO_INCREMENT PRIMARY KEY, discord_id INT, name TINYTEXT, def DOUBLE)")
    #mycursor.execute("CREATE TABLE armor (id INT AUTO_INCREMENT PRIMARY KEY, discord_id INT, name TINYTEXT, hp DOUBLE, def DOUBLE, evasion DOUBLE, ishelmet BOOL, isChestplate BOOL, isLeggins BOOL, isBoots BOOL)")

    #mycursor.execute("CREATE TABLE playeritems (id INT AUTO_INCREMENT PRIMARY KEY, discord_id INT, name TINYTEXT, ALLE IDs)")


    sql = "INSERT INTO mobs (name, hp, hpfactor, dmg, dmgfactor, def, deffactor, evasion, evasionfactor, aim, aimfactor, xp, xpfactor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = ("Zombie", 20.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 5.0, 1.1)

    mycursor.execute(sql, val)

    val = ("Creeper", 18.0, 1.1, 3.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 5.0, 1.1)

    mycursor.execute(sql, val)

    val = ("Skeleton", 20.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 5.0, 1.1)

    mycursor.execute(sql, val)

    val = ("Enderman", 30.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 10.0, 1.1)

    mycursor.execute(sql, val)
    mydb.commit()