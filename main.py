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
                    iHP = message.embeds[0].fields[0].value
                    iHP = int(iHP) - 8
                    message.embeds[0].set_field_at(0, name = "HP", value = iHP)
                    await message.edit(embed=message.embeds[0])

                await message.remove_reaction(payload.emoji, payload.member)
    return

@bot.command(aliases=["t"])
async def test(ctx, arg=None):
    embed = discord.Embed(title="Creeper", color=0xedbc5d)
    embed.set_thumbnail(url="https://images-na.ssl-images-amazon.com/images/I/51UntwGjyzL._AC_SL1000_.jpg")
    embed.set_author(name="Monster")
    embed.add_field(name="HP", value="100", inline=True)
    embed.add_field(name="Level", value="15", inline=True)
    newmessage = await ctx.send(embed=embed)
    #await ctx.send("Test")
    await newmessage.add_reaction('<:Sword:781239337815769098>')



bot.run(token)
