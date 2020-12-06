import discord
import json

from discord.ext import commands
from discord.utils import get

with open('config/config.json') as json_file:
    jsonstructure = json.load(json_file)
    for p in jsonstructure['discord']:
        token = p['token']

bot = commands.Bot(command_prefix='!', case_insensitive=True, help_command=None)

@bot.event
async def on_ready():
    print('Bot wurde gestartet')
    return

@bot.event
async def on_raw_reaction_add(payload):


    if(payload.member != bot.user):
        if payload.channel_id == 781229072092233748:
            if payload.emoji.id == 781239337815769098:
                channel = bot.get_channel(payload.channel_id)
                message = await channel.fetch_message(payload.message_id)
                if(message.embeds):
                    #await channel.send(message.embeds[0].author.name)
                    #await channel.send("FUNKTIONIERT!")
                    embed = message.embeds[0]
                    iHP = int(embed.fields[0].value) - 8
                    if(iHP < 0):
                        iHP = 0
                    pname = 100
                    sfile = None
                    sfilename = None
                    surl = None
                    if(iHP >= 75):
                        pname = 75
                    elif(iHP >= 50):
                        pname = 50
                    elif(iHP >= 25):
                        pname = 25
                    else:
                        pname = 0
#                    sfile = "pictures/health/" + str(pname) + ".png"
#                    sfilename = str(pname) + ".png"
                    surl = "https://blizzor.de/MineLife/" + str(pname) + ".png" 
#                    surl = "attachment://" + str(pname) + ".png"
#                    file = discord.File(sfile, filename=sfilename)

                    embed.set_thumbnail(url=surl)
                    embed.set_field_at(0, name = "HP", value = iHP)
                    await message.edit(embed=embed)

                await message.remove_reaction(payload.emoji, payload.member)
    return

@bot.command(aliases=["t1"])
async def test1(ctx, arg=None):
    embed = discord.Embed(title="Creeper", color=0xedbc5d)
    embed.set_thumbnail(url="https://images-na.ssl-images-amazon.com/images/I/51UntwGjyzL._AC_SL1000_.jpg")
    embed.set_author(name="Monster")
    embed.add_field(name="HP", value="100", inline=True)
    embed.add_field(name="Level", value="15", inline=True)
    newmessage = await ctx.send(embed=embed)
    #await ctx.send("Test")
    await newmessage.add_reaction('<:Sword:781239337815769098>')

@bot.command(aliases=["t2"])
async def test2(ctx, arg=None):

    #file = discord.File("pictures/health/100.png", filename="100.png")

    embed = discord.Embed(title="Creeper", color=0xedbc5d)
    #embed.set_thumbnail(url="attachment://100.png")
    embed.set_thumbnail(url="https://blizzor.de/MineLife/100.png" )
    
    embed.set_author(name="Monster")
    embed.add_field(name="HP", value="100", inline=True)
    embed.add_field(name="Level", value="15", inline=True)
    newmessage = await ctx.send(embed=embed)
    #await ctx.send("Test")
    
    await newmessage.add_reaction('<:Sword:781239337815769098>')


bot.run(token)
