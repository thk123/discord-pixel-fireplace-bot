import os

import discord
from dotenv import load_dotenv


def extract_message(message_body, prefix):
    if message_body.startswith(prefix):
        return str.strip(message_body[len(prefix):])
    return None


def is_arrow_keys(command):
    return command in {'up', 'down', 'left', 'right'}


def main():
    # have to import in this scope as requires a GUI to import(!)
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

        command = extract_message(message.content, '!')
        if command:
            response = 'Executing fire command: ' + command
            typewrite(command)

            print(response)
            await message.channel.send('Doing some firey stuff')

    client.run(TOKEN)


if __name__ == "__main__":
    main()
