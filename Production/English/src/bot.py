# Libraries importation
import discord
from src.commands import commandHandler

# Definition of the Discord parameters
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("bot is ready !")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content[0:1] == '!':
        message.content = message.content[1:]
        await commandHandler(message)  # Use of the 'await' command to call the coroutine