import discord
import os

client = discord.Client()

token = os.getenv('DISCORD_BOT_TOKEN')

client.tally = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inc'):
        client.tally += 1
        await message.channel.send("The current tally is: " + str(client.tally))

    if message.content.startswith('$set'):
        client.tally = int(message.content[5:])
        await message.channel.send("The current tally is: " + str(client.tally))

client.run(token)