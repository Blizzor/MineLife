import discord
import json
import mysql.connector

from discord.ext import commands
from discord.utils import get
from modules import functions
from modules import database
from modules import mobs
from modules import init

intents = discord.Intents.all()

token = init.configs["token"]
DBhost = init.configs["DBhost"]
DBuser = init.configs["DBuser"]
DBpasswd = init.configs["DBpasswd"]
DBdatabase = init.configs["DBdatabase"]
IDChannelSpawner = init.configs["IDChannelSpawner"]
IDEmote = init.configs["IDEmote"]
NameEmote = init.configs["NameEmote"]

bot = commands.Bot(command_prefix='!', case_insensitive=True, help_command=None, intents=intents)

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
    if ctx.message.channel.id == IDChannelSpawner:
        newmessage = await functions.spawnmob(ctx)
        await newmessage.add_reaction("<:" + NameEmote + ":" + str(IDEmote) + ">")
    return

<<<<<<< Updated upstream
@bot.command(aliases=["resetDatabase"])
async def resetDb(ctx, arg=None):
    await database.resetDb()
=======
@bot.command(aliases=["resetdatabase"])
async def resetdb(ctx, arg=None):
    await database.resetDatabase()
>>>>>>> Stashed changes
    return

bot.run(token)
