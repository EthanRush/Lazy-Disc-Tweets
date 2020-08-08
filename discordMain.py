import discord
import config
import asyncio
import sys
import twitterMain

client = discord.Client()

picExt = ['jfif', 'pjepg', 'jpeg', 'pjp', 'jpg', 'png', 'webp']
videoExt = ['gif', 'm4v', 'mp4', 'mov', 'webm']



# obtains the URL for a discord attachment
def getUrl(msg):
    return msg.attachments[0].url

# obtains the file extension type given a url
def getExtension(url):
    return url.rsplit('.', maxsplit = 1)[1]

# checks if a message is a discord attachment
def isDiscordAttachment(msg):
    return len(msg.attachments) > 0 

def isValidAttachment(msg, extList):
    return getExtension(getUrl(msg)).lower() in extList





@client.event
async def on_ready():
    print('{.user} stuck the superhero landing'.format(client))

@client.event
async def on_message(message):
    
    #checks if the message is from the original message
    def isOp(msg):
        return msg.author == message.author

    def picNumCheck(msg):
        return isOp(msg) and msg.content.isnumeric() and int(msg.content) <= 4 and int(msg.content) > 0

    def mediaCheck(msg):
        return isOp(msg) and isDiscordAttachment(msg) and isValidAttachment(msg, picExt)

    def videoCheck(msg):
        return isOp(msg) and isDiscordAttachment(msg) and isValidAttachment(msg, videoExt)
    
    #KNOWN ERROR: IF user resonds with one of the commands it summons another insance (Ex: for text status user repsponds with !postTextTweet)
    async def responseTemplate(checkType, response):
        try:
            msg = await client.wait_for('message', timeout=60.0, check=checkType)

        except asyncio.TimeoutError:
            await msg.channel.send("Timeout, tweet has been terminated")

        else:
            if len(response) > 0:
                await msg.channel.send(response)
            return msg



    if message.author == client.user:
        return 

   
    
    #For posting tweets with no photos or videos
    if message.content.startswith('!postTextTweet'):
        await message.channel.send('Please type out the text for the tweet you want to post')
        
        msg1 = await responseTemplate(isOp, '')
        if msg1:
            await message.channel.send('Tweet posted: https//www.twitter.com/{0}'.format(twitterMain.postTweet(msg1.content, []))) 

    #For posting tweets with text and photos 
    if message.content.startswith('!postPhotoTweet'):
        
        await message.channel.send('Please type out the text status surrounded by quotes (Example: "XXXXX")')

        msg1 = await responseTemplate(isOp, 'How many photos will be included in this tweet? (0-4)')
        if msg1:
            
            statusText = msg1.content

            msg2 = await responseTemplate(picNumCheck, 'Please send photo(s), uploaded as seperate discord attachments')
            if msg2:
                picsLeft = int(msg2.content)
                picIds = []
                while picsLeft > 0:
                    msg3 = await responseTemplate(mediaCheck,'{0} pictures left'.format(picsLeft-1))
                    if msg3:

                        #TODO pass twitter bot the photos and return the id with upload_media()
                        picIds.append(twitterMain.getId(msg3.attachments[0].url , False))  
                        picsLeft -= 1

                await message.channel.send('Tweet posted: https//www.twitter.com/{0}'.format(twitterMain.postTweet(statusText, picIds)))
    
    
    if message.content.startswith('!postVideoTweet'):
        await message.channel.send('Please type out the text for the tweet you want to post')

        msg1 = await responseTemplate(isOp, 'Please send the video as a discord attachment')
        if msg1:
            statusText = msg1.content
            picIds = []
            msg2 = await responseTemplate(videoCheck, 'Video recieved')
            if msg2:
                picIds.append(twitterMain.getId(msg2.attachments[0].url , True))
                 
                #  Then use update_status(status= tempText, media_ids=","".join(picIds))
                # NOTE depending on how IDs are returned may need to force them to be strings 

                await message.channel.send('Tweet posted: https//www.twitter.com/{0}'.format(twitterMain.postTweet(statusText, picIds))) 

    if message.content.startswith('!commitDie'):
        await message.channel.send('If you insist')
        await message.channel.send('*Tweetcord is going offline*')
        sys.exit()

client.run(config.clientToken)