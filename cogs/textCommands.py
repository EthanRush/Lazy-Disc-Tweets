import discord
import os
from discord.ext import commands

class textTweet(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    async def text(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Forgetting something? \n*Error: no subcommand issued*')