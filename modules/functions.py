import discord
from random import randrange

from modules import init

async def spawnmob(ctx):
    number = randrange(1,5)
    sql = "SELECT * FROM mobs WHERE id ='" + str(number) + "'"
    myresult = await dbcommit(sql)
    mob = myresult[0]
    mobname = mob[1]
    mobhp = mob[2]

    embed = discord.Embed(title=mobname, color=0x00ff00)
    embed.set_thumbnail(url="https://blizzor.de/MineLife/"+ mobname +".png")
    embed.set_author(name="Monster")
    embed.add_field(name="HP", value=mobhp, inline=True)
    embed.add_field(name="Level", value="15", inline=True)
    newmessage = await ctx.send(embed=embed)
    #await newmessage.add_reaction('<:Sword:781239337815769098>')
    return newmessage

async def on_attack(payload,bot):
    if payload.member != bot.user:
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        if(message.embeds):
            embed = message.embeds[0]
            iHP = float(embed.fields[0].value) - 8
            color=0xedbc5d
            if(iHP > 0):
                surl = None
                colorx = 0
                colory = 255
                colorz = "00"
                if(iHP <= 100 and iHP > 50):
                    colorx = int(float(255)-((float(iHP)-float(50))*5.1))
                elif(iHP <=50 and iHP > 0):
                    colorx = 255
                    colory = int((float(iHP))*5.1)
                else:
                    colorx = 0
                    colory = 0

                if(colorx != 0):
                    colorx = str(hex(colorx)).removeprefix("0x")
                else:
                    colorx = "00"

                if(colory != 0):
                    colory = str(hex(colory)).removeprefix("0x")
                else:
                    colory = "00"

                color = "0x" + colorx + colory + colorz

                color = int(color, 0)

                surl = "https://blizzor.de/MineLife/" + embed.title + ".png" 

                embed = discord.Embed(title = embed.title, color = color)
                embed.set_thumbnail(url=surl)
                embed.set_author(name="Monster")
                embed.add_field(name="HP", value=iHP, inline=True)
                embed.add_field(name="Level", value="15", inline=True)
                await message.edit(embed=embed)

                await message.remove_reaction(payload.emoji, payload.member)
            else:
                await message.delete()
                await on_death(message)

    return

async def on_death(message):
    embed = discord.Embed(title = "Loot", color = 0x6f4d08)
    embed.add_field(name="Frederik", value="2 x Bone", inline=False)
    embed.add_field(name="Horst", value="5 x Stone", inline=False)
    await message.channel.send(embed = embed)
    return

async def dbcommit(sqlcommand):
    try:
        mydb = init.getdb()
        mycursor = mydb.cursor()
        mycursor.execute(sqlcommand)
        return mycursor.fetchall()
    except Exception:
        if(not mydb.is_connected):
            init.reconnect()
            mydb = init.getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sqlcommand)
            return mycursor.fetchall()
