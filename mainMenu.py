import discord
import os
import utilDisc
import tweetCommands
from discord.ext import commands

class mainMenu(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    async def post(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Forgetting something? \n*Error: no subcommand issued*')

    @commands.group()
    async def testAuth(self, ctx):
        await ctx.send(ctx.message.author)

    @post.command()
    async def tweet(self, ctx):
        
        
        self.client.load_extension('tweetCommands')
        self.client.unload_extension('mainMenu')
        await ctx.send('Commands for tweeting are ready and mainMenu commands are locked!')


def setup(client):
    client.add_cog(mainMenu(client))

