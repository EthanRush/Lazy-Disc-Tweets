import discord
import os
import utilDisc
import twitterMain
from discord.ext import commands


class tweetCommands(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.author = None
        self.status = None
        self.photos = []

    @commands.group()
    async def twit(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Forgetting something? \n*Error: no subcommand issued*')

    @commands.group()
    async def setOP(self, ctx):
        self.author = ctx.message.author

    @twit.command()
    async def setStatus(self, ctx, *, statusText):
        if await utilDisc.isOp(self.author, ctx):
            if self.status == None:
                self.status = statusText
                await ctx.send('Status text has been set')
            else:
                self.status = statusText
                await ctx.send('Status text has been updated')
    
    @twit.command()
    async def preview(self, ctx):
        if await utilDisc.isOp(self.author, ctx):
            await ctx.send('Tweet preview: \n\n From Discord User: {0} \n\n Tweet Status: {1}'.format(self.author, self.status))

    @twit.command()
    async def post(self, ctx):
        if await utilDisc.isOp(self.author, ctx):
            tempObj = twitterMain.postTweet(self.status, self.photos)
            await ctx.send('Tweet posted: https://twitter.com/{0}/status/{1}'.format(tempObj['user']['screen_name'], tempObj['id_str']))
            self.client.load_extension('mainMenu')

def setup(client):
    client.add_cog(tweetCommands(client))

