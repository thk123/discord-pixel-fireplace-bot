import os

import discord
from dotenv import load_dotenv

from pyautogui import typewrite

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        print('The following guilds are using the server: ' + str(guild))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        response = 'Executing fire command: ' + message.content
        typewrite(message.content)

        print(response)
        await message.channel.send('Doing some firey stuff')


client.run(TOKEN)
