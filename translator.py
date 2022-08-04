import os
import discord
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
    role = discord.utils.get(message.author.roles, name='uwu prison')
    if role is not None and role.name == 'uwu prison':
        uwu_flags = uwuify.SMILEY | uwuify.YU
        cursed_payload = uwuify.uwu(message.content, flags=uwu_flags)
        channel = message.channel
        async with channel.typing():
            await message.reply(cursed_payload)







client.run(token)