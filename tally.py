import discord

client = discord.Client()

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

client.run('ODUzNzg2MzE3MjU5NjY5NTI0.YMaceA.itRy4aT2ZSepVJHADFClN17LVrs')