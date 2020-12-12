import discord
import json
import mysql.connector

from discord.ext import commands
from discord.utils import get
from modules import functions
from modules import mobs

with open('config/config.json') as json_file:
    jsonstructure = json.load(json_file)
    for p in jsonstructure['discord']:
        token = p['token']
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

bot = commands.Bot(command_prefix='!', case_insensitive=True, help_command=None)

@bot.event
async def on_ready():
    print('Bot wurde gestartet')
    return

@bot.event
async def on_raw_reaction_add(payload):

    await functions.on_attack(payload,bot)
    #await functions.on_attack2(payload,bot)
    
    return

@bot.command(aliases=["t1"])
async def test1(ctx, arg=None):
    await functions.spawnmob(ctx, mydb)
    return

@bot.command(aliases=["t2"])
async def test2(ctx, arg=None):
    await functions.spawnmob2(ctx)
    return

bot.run(token)
