import discord
import config
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('{.user} stuck the superhero landing'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!postTextTweet'):
        await message.channel.send('Please type out the text for the tweet you want to post')
        
        def statusCheck(msg1):
            return msg1.author == message.author

        try:
            msg1 = await client.wait_for('message', timeout=60.0, check=statusCheck)

        except asyncio.TimeoutError:
            await message.channel.send("Timeout, tweet has been terminated")

        else:

            #TODO twitterBot.updateStatus(message.content)
            await message.channel.send('Tweet posted: https//www.twitter.com/') # TODO .format(twitterBot.getLastTweetId())) 
            
    if message.content.startswith('!postPhotoTweet'):
        await message.channel.send('Please type out the text for the tweet you want to post')

        def statusCheck(msg1):
            return msg1.author == message.author

        try:
            msg1 = await client.wait_for('message', timeout=60.0, check=statusCheck)

        except asyncio.TimeoutError:
            await message.channel.send("Timeout, tweet has been terminated")

        else:

            statusText = msg1.content
            await message.channel.send('How many photos will be included in this tweet? (0-4)')

            def picNumCheck(msg2):
                return msg2.author == message.author and msg2.content.isnumeric() and int(msg2.content) <= 4

            try:
                msg2 = await client.wait_for('message', timeout=60.0, check=picNumCheck)

            except asyncio.TimeoutError:
                await message.channel.send("Timeout, tweet has been terminated")

            except:
                await message.channel.send('ERROR: user does not know how to follow instructions, terminating post')

            else:

                picsLeft = int(msg2.content)
                picIds = []
                await message.channel.send('Please send {0} photos, uploaded as seperate discord attachments'.format(picsLeft))

                def mediaCheck(msg3):
                    return msg3.author == message.author #and msg3.content.startswith('https://cdn.discordapp.com/attachments/')

                for i in range(picsLeft, 0, -1):
                    try:
                        msg3 = await client.wait_for('message', timeout=60.0, check=mediaCheck)

                    except asyncio.TimeoutError:
                        await message.channel.send("Timeout, tweet has been terminated")

                    else:
                        print(msg3.content) #TO DO FIGURE OUT HOW TO OBTAIN LINK FROM IMAGES (DON'T SHOW UP UNDER MESSAGE.CONTENT)
                        picIds.append('') #TODO pass twitter bot the message.content and return the id with upload_media()

                # have twitterBot use update_status(status= tempText, media_ids=","".join(picIds))
                # NOTE depending on how IDs are returned may need to force them to be strings in the list

                await message.channel.send('Tweet posted: https//www.twitter.com/') # TODO .format(twitterBot.getLastTweetId())) 


    if message.content.startswith('!postVideoTweet'):
        await message.channel.send('Please type out the text for the tweet you want to post')

        def statusCheck(msg1):
            return msg1.author == message.author

        try:
            msg1 = await client.wait_for('message', timeout=60.0, check=statusCheck)

        except asyncio.TimeoutError:
            await message.channel.send("Timeout, tweet has been terminated")

        else:
            statusText = msg1.content
            await message.channel.send('Please send the video as a discord attachment')

            def mediaCheck(msg2):
                 return p.user == message.author and p.content.startswith('https://cdn.discordapp.com/attachments/')

            try:
                msg2 = await client.wait_for('message', timeout=60.0, check=mediaCheck)

            except asyncio.TimeoutError:
                await message.channel.send("Timeout, tweet has been terminated")

            else:
                #  Pass twitterBot the message.content and use upload_video() 
                #  Then use something update_status(status= tempText, media_ids=","".join(picIds))
                # NOTE depending on how IDs are returned may need to force them to be strings 

                await message.channel.send('Tweet posted: https//www.twitter.com/') # TODO .format(twitterBot.getLastTweetId())) 

client.run(config.clientToken)