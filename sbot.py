# bot.py
import os

import discord
import numpy as np
from dotenv import load_dotenv
import time
import re

import scrabblebag

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

#mybag = scrabblebag.scrabble_bag(2)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the awesome Scrabble server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'start new game':
    	response = 'have you forgotten your manners'
    	await message.channel.send(response)

    if message.content == 'start new game, please':
    	response = 'starting new game'
    	tmp = int(time.time())
    	global mybag
    	mybag = scrabblebag.scrabble_bag(2, seed = tmp)
    	response += str(len(mybag)) + str(tmp)
    	await message.channel.send(response)

    if re.match('draw.', message.content):
        indx = int(message.content[-1])
        response = mybag.remove(indx, show = True)
        #response = message.content[-1]
        await message.channel.send(response)

    if message.content == 'howmuchugot':
    	response = len(mybag)
    	await message.channel.send(response)

    if message.content == 'oops':
    	response = "I can forgive stupid as long as it's temporary"
    	await message.channel.send(response)
client.run(TOKEN)