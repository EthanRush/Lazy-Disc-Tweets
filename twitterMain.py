import config
from twython import Twython, TwythonError

twitter = Twython(config.twitterAppKey, config.twitterAppSecret, config.twitterOauthToken, config.twitterOauthTokenSecret)


async def getTweets():
    return twitter.get_user_timeline(user_id=twitter)

async def getId(fileLink, fileType, isVideo:bool):
    postMedia = open(fileLink, 'rb')
    if isVideo:
        return twitter.upload_video(media=postMedia, media_type='video/{0}'.format(fileType))
    else:
        return twitter.upload_media(media=postMedia)


def postTweet(statusText:str, mediaIds:list):
    try: 
        return twitter.update_status(status=statusText, media_ids=mediaIds)['id_str']
    except TwythonError as e:
        print(e)