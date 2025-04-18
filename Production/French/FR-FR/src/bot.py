# Libraries importation
import discord
from src.commands import commandHandler

# Définition des parametres de Discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content[0:1] == '!':
        message.content = message.content[1:]
        await commandHandler(message)  # Utiliser la commande 'await' pour lancer la coroutine