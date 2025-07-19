import discord
import os
import logging
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
logging.basicConfig(level=logging.INFO, handlers=[handler])
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Ready!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        raise ValueError("Token não existe!")

    await load_cogs()
    await bot.start(token)

import asyncio
asyncio.run(main())