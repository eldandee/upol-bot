import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime
from discord.utils import get

bot = commands.Bot(command_prefix='!')
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
    print(
        f'{bot.user} is connected to the following guild:'
    )

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(735899091371819032)
    role = get(member.guild.roles, name="Student")
    await channel.send(f'Ahoj {member.mention}, vítej na UPOL serveru!')
    await member.add_roles(role)

@bot.command(name="help", pass_context=True)
async def prikazy(ctx):
    response = '**Nápověda:**\n\
    *!help* - vypíše seznam příkazů\n'
    await ctx.send(response)

@bot.command(name="purge",pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.message.delete()

@bot.command(name="tyden", pass_context=True)
async def prikazy(ctx):
    year, tyden, day_of_week = datetime.datetime.today().isocalendar()
    response="Je "
    if tyden % 2 == 0:
        response+="sudý "
    else:
        response+="lichý "
    response+="týden."
    await ctx.send(response)

bot.run('NzM1ODk1MTg3OTc2NDg3MDIz.XxnSWg.m0fFnI0w7xEzF_KBbeMNrbVsX_Y')
