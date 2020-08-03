import discord
import os
import utilDisc
from discord.ext import commands

class tweet:

    def __init__(self,  op: author):
        self.status = ''
        self.photoNum = 0
        self.photos = []
        self.op = op

    


class photoTweet(commands.Cog):

    tweet = {}    

    def create(self, author_id ):
        tweet[author_id] = tweet(author_id)


    @commands.group()
    async def photoTweet(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Forgetting something? \n*Error: no subcommand issued*')

    @photoTweet.command()
    async def setStatus(self, ctx, *, statusText):
        self.status = statusText
        

    @photoTweet.command()
    async def setPhotos(self, ctx, pNum):
        self.photoNum = pNum
        await self.addPhotos(ctx)

    

    async def addPhotos(self, ctx):
        
        while self.photoNum > 0:
            msg = await utilDisc.responseTemplate(utilDisc.mediaCheck,'{0} pictures left'.format(self.photoNum-1), self)
            if msg:
                        
                print(msg.attachments[0].url) 
                self.photos.append('') #TODO pass twitter bot the url and return the id with upload_media()
                self.photoNum -= 1

def setup(client):
    client.add_cog(photoTweet(client))  