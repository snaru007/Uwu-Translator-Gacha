import os
import discord
import random
import uwuify
from dotenv import load_dotenv

#load discord bot
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.content:
        return
    if not ' ' in message.content.strip():
        return 
    role = discord.utils.get(message.author.roles, name='Weebs')
    gachaWin = (random.randrange(100) == 69)
    if role is not None and role.name == 'Weebs' and gachaWin:
        uwu_flags = uwuify.SMILEY | uwuify.YU
        if uwuify.uwu(message.content) == message.content:
            return
        cursed_payload = uwuify.uwu(message.content, flags=uwu_flags)
        channel = message.channel
        async with channel.typing():
            await message.reply(cursed_payload)







client.run(token)