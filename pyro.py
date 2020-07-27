import os

import discord
from dotenv import load_dotenv


def extract_message(message_body, prefix):
    if message_body.startswith(prefix):
        return str.strip(message_body[len(prefix):])
    return None


def is_arrow_keys(command):
    return command.lower() in {'up', 'down', 'left', 'right'}


def is_valid_command(command:str):
    if len(command) > 30:
        return False

    banned_commands = {'shutdown'}

    return all(banned_command not in command.lower() for banned_command in banned_commands)


def main():
    # have to import in this scope as requires a GUI to import(!)
    from pyautogui import typewrite, press

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

        # We're only interested in messages in the #firepit channel
        if message.channel != 'firepit':
            return

        command = extract_message(message.content, '!')
        if command:
            if is_arrow_keys(command):
                print('Pressing arrow keys: ' + command)
                press(command)
                await message.add_reaction('🔥')
            elif is_valid_command(command):
                print('Executing fire command: ' + command)
                typewrite(command)
                await message.add_reaction('🔥')
            else:
                print('Ignoring command: ' + command)
                await message.add_reaction('❌')

    client.run(TOKEN)


if __name__ == "__main__":
    main()
