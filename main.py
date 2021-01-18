import discord
import json
import mysql.connector

from discord.ext import commands
from discord.utils import get
from modules import functions
from modules import mydatabase
from modules import mobs
from modules import init

intents = discord.Intents.all()

token = init.config().get_token()
DBhost = init.config().get_DBhost()
DBuser = init.config().get_DBuser()
DBpasswd = init.config().get_DBpasswd()
DBdatabase = init.config().get_DBdatabase()
IDChannelSpawner = init.config().get_IDChannelSpawner()
IDEmote = init.config().get_IDEmote()
NameEmote = init.config().get_NameEmote()

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

@bot.command(aliases=["syncdatabase"])
async def syncdb(ctx, arg=None):
    await mydatabase.installdb()
    return

bot.run(token)
