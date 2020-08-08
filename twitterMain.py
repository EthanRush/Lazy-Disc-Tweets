import config
import mimetypes
import requests
from twython import Twython, TwythonError

twitter = Twython(config.twitterApiKey, config.twitterApiSecret, config.twitterAccessToken, config.twitterAccessSecret)

def getId(fileLink, isVideo:bool):
    
    name = fileLink.split('/')[-1]
    with open(name, 'wb') as f:
        f.write(requests.get(fileLink).content)

    postMedia = open (name, 'rb')

    if isVideo:
        return twitter.upload_video(media=postMedia, media_type=mimetypes.guess_type(fileLink))['media_id_string']
    else:
        return twitter.upload_media(media=postMedia)['media_id_string']


def postTweet(statusText:str, mediaIds:list):
    try: 
        return twitter.update_status(status=statusText, media_ids=mediaIds)['id_str']
    except TwythonError as e:
        print(e)