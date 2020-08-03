import discord
import os
import photoCommands
from discord.ext import commands

class basicTweet(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    async def post(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Forgetting something? \n*Error: no subcommand issued*')

    @post.command()
    async def text(self, ctx):
        self.client.load_extension('cogs.textCommands')
        photoCommands.photoTweet.create(ctx.author)
        self.client.unload_extension('cogs.basicTweetCommands')
        ctx.send('Commands for text post ready and basicTweet commands locked!')

    @post.command()
    async def photo(self, ctx):
        self.client.load_extension('cogs.photoCommands')
        self.client.unload_extension('cogs.basicTweetCommands')
        ctx.send('Commands for photo post ready and basicTweet commands locked!')


    @post.command()
    async def video(self, ctx):
        self.client.load_extension('cogs.videoCommands')
        self.client.unload_extension('cogs.basicTweetCommands')
        ctx.send('Commands for video post ready and basicTweet commands locked!')




