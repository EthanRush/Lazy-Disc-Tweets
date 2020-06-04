import discord
import config

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} stuck the superhero landing'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!test'):
        await message.channel.send('I am here if you need to talk')

client.run(config.clientToken)
