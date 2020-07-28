import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime
import requests
from discord.utils import get
from config import Config

load_dotenv()
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix=Config.prefix)
bot.remove_command('help')


def open_json():
    with open('upol.json') as json_file:
        data = json.load(json_file)
    return data


def save_json(data):
    with open('upol.json', 'w') as outfile:
        json.dump(data, outfile)


def open_db():
    client = pymongo.MongoClient(MONGODB_URI)
    db = client.get_default_database()
    upol = db[DB_NAME]
    return client, upol


def read_db():
    client, upol = open_db()
    data = upol.find_one()
    client.close()
    return data


@bot.event
async def on_ready():
    print(f'{bot.user} is connected to the following guild:')
    for guild in bot.guilds:
        print(
            f"{guild.name} with members_count: {guild.member_count} and owner: {str(guild.owner)}")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(735899091371819032)
    role = get(member.guild.roles, name="Student")
    await channel.send(f'Ahoj {member.mention}, vítej na UPOL serveru!')
    await member.add_roles(role)


@bot.command(name="help", pass_context=True)
async def prikazy(ctx):
    response = '**Nápověda:**\n\
    !help - vypíše seznam příkazů\n\
    !tyden - vypíše kalendáří týden v roce\n\
    !pocasi \{město\} - vypíše počasí v zadaném městě\n'
    await ctx.send(response)


@bot.command(name="purge", pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    await ctx.message.delete()


@bot.command(name="tyden", pass_context=True)
async def prikazy(ctx):
    year, tyden, day_of_week = datetime.datetime.today().isocalendar()
    if tyden % 2 == 0:
        cal_type = "Sudý"
    else:
        cal_type = "Lichý"
    embed = discord.Embed(title="Týden", color=0xE5DC37)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=str(ctx.author))
    embed.add_field(name="Kalendářní", value="{} ({})".format(cal_type, tyden))
    await ctx.send(embed=embed)


@bot.command(name="pocasi", pass_context=True)
async def weather(ctx, *args):
    token = '65b5078cfd3c4d143c2fa40d34377ef1'
    city = "Brno"
    if len(args) != 0:
        city = " ".join(map(str, args))
    url = (
        "http://api.openweathermap.org/data/2.5/weather?q="
        + city
        + "&units=metric&lang=cz&appid="
        + token
    )
    res = requests.get(url).json()

    if str(res["cod"]) == "200":
        description = "Aktuální počasí v městě " + \
            res["name"] + ", " + res["sys"]["country"]
        embed = discord.Embed(title="Počasí", description=description)
        image = "http://openweathermap.org/img/w/" + \
            res["weather"][0]["icon"] + ".png"
        embed.set_thumbnail(url=image)
        weather = res["weather"][0]["main"] + \
            " (" + res["weather"][0]["description"] + ") "
        temp = str(res["main"]["temp"]) + "°C"
        feels_temp = str(res["main"]["feels_like"]) + "°C"
        humidity = str(res["main"]["humidity"]) + "%"
        wind = str(res["wind"]["speed"]) + "m/s"
        clouds = str(res["clouds"]["all"]) + "%"
        visibility = str(res["visibility"] / 1000) + \
            " km" if "visibility" in res else "bez dat"
        embed.add_field(name="Počasí", value=weather, inline=False)
        embed.add_field(name="Teplota", value=temp, inline=True)
        embed.add_field(name="Pocitová teplota", value=feels_temp, inline=True)
        embed.add_field(name="Vlhkost", value=humidity, inline=True)
        embed.add_field(name="Vítr", value=wind, inline=True)
        embed.add_field(name="Oblačnost", value=clouds, inline=True)
        embed.add_field(name="Viditelnost", value=visibility, inline=True)
        await ctx.send(embed=embed)
    elif str(res["cod"]) == "404":
        await ctx.send("Město nenalezeno")
    elif str(res["cod"]) == "401":
        await ctx.send("Rip token -> Rebel pls fix")
    else:
        await ctx.send(
            "Město nenalezeno! <:pepeGun:484470874246742018> (" +
            res["message"] + ")"
        )

bot.run(Config.token)
