import discord
import time
import os
from config import config as c
import sevenseq.sevenseq as sevenseq

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_voice_state_update(member, before, after):
        if(before.channel == after.channel):
            return
        if(member.voice == None):
            await client.get_channel(c.logging_channel).send(member.name + " has left")
            print(member.name + " has left")
        else:
            await client.get_channel(c.logging_channel).send(member.name + " has joined")
            print(member.name + " has joined")
        try:
            sevenseq.setnum(len(after.channel.members))
        except:
            sevenseq.setnum(len(before.channel.members))

client.run(c.token)