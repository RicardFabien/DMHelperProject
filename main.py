# bot.py
import os
import random

import discord
from dotenv import load_dotenv

from MesageHandler import MessageHandler

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

message_handler = MessageHandler()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    print("Reçu " + message.content)



    response = message_handler.handle_message(message.content)
    if response :
        await message.channel.send(response)

client.run(TOKEN)
