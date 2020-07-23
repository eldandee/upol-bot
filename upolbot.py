import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!')

token = os.getenv('DISCORD_TOKEN')
@bot.event
async def on_ready():
    print("Hello")

bot.run('NzM1ODk1MTg3OTc2NDg3MDIz.Xxm6AQ.5AzEyH90tW2RsulVUjU5QUsjQWM')
