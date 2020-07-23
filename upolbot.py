import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Hello")

bot.run('PCuXv0a-LsKz4XTEIEwR7ir3i8YH-1oN')
