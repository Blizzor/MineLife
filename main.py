import discord
import json
import mysql.connector

from discord.ext import commands
from discord.utils import get
from modules import functions
from modules import mydb
from modules import mobs

with open('config/config.json') as json_file:
    jsonstructure = json.load(json_file)
    for p in jsonstructure['discord']:
        token = p['token']
        DBhost = p['DBhost']
        DBuser = p['DBuser']
        DBpasswd = p['DBpasswd']
        DBdatabase = p['DBdatabase']
        IDChannelSpawner = p['IDChannelSpawner']
        IDEmote = p['IDEmote']
        NameEmote = p['NameEmote']



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
    if payload.channel_id == IDChannelSpawner and payload.emoji.id == IDEmote:
        await functions.on_attack(payload,bot)
    
        return

@bot.command(aliases=["t1"])
async def test1(ctx, arg=None):
    newmessage = await functions.spawnmob(ctx, mydb)
    await newmessage.add_reaction("<:" + NameEmote + ":" + str(IDEmote) + ">")
    return

@bot.command(aliases=["syncdatabase"])
async def syncdb(ctx, arg=None):
    await mydb.installdb()
    return

bot.run(token)
