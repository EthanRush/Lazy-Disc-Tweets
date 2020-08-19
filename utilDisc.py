import discord
import config
import asyncio
import sys

picExt = ['jfif', 'pjepg', 'jpeg', 'pjp', 'jpg', 'png', 'webp']
videoExt = ['gif', 'm4v', 'mp4', 'mov', 'webm']

# obtains the URL for a discord attachment
async def getUrl(msg):
    return msg.attachments[0].url

# obtains the file extension type given a url
async def getExtension(url):
    return url.rsplit('.', maxsplit = 1)[1]

# checks if a message is a discord attachment
async def isDiscordAttachment(msg):
    return len(msg.attachments) > 0 

async def isValidAttachment(msg, extList):
    return getExtension(getUrl(msg)).lower() in extList

#checks if the message is from the original message
async def isOp(auth, message):
    return auth == message.author

async def picNumCheck(msg, message):
     return isOp(msg, message) and msg.content.isnumeric() and int(msg.content) <= 4 and int(msg.content) > 0

async def mediaCheck(msg, message):
    return isOp(msg, message) and isDiscordAttachment(msg) and isValidAttachment(msg, picExt)

async def videoCheck(msg, message):
    return isOp(msg, message) and isDiscordAttachment(msg) and isValidAttachment(msg, videoExt)

#KNOWN ERROR: IF user resonds with one of the commands it summons another insance (Ex: for text status user repsponds with !postTextTweet)
async def responseTemplate(checkType, response, client):
    try:
        msg = await client.wait_for('message', timeout=60.0, check=checkType)

    except asyncio.TimeoutError:
        await msg.channel.send("Timeout, tweet has been terminated")

    else:
        if len(response) > 0:
            await msg.channel.send(response)
        return msg