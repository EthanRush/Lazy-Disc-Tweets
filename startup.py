import discord
import os
import sys
import config
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'{extension}')
    await ctx.send(f'{extension} has been loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'{extension}')
    await ctx.send(f'{extension} has been unloaded')

@client.command()
async def reload(ctx, extension):
    client.reload_extension(f'{extension}')
    await ctx.send(f'{extension} has been reloaded, any changes made will now be available')


@client.command()
async def exit(ctx):
    await ctx.send('Shutting Down')
    sys.exit()

@client.event
async def on_ready():
    print('{.user} stuck the superhero landing'.format(client))
    

client.load_extension('mainMenu')

client.run(config.clientToken)