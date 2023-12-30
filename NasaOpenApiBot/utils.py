from tweepy_manager import TweepyManager
import logging
import requests
import io

tw_manager = TweepyManager()

def create_APOD_tweet(data):
    tweepy_client = tw_manager.get_tweepy_client()
    tweepy_api = tw_manager.get_tweepy_api_1()
    tweet = "Date: {0}\nTitle: {1}\nUrl: {2}\n#APOD #NASA @NASA".format(
        data['date'], data['title'], data['url'])
    if data['media_type'] == 'image':
        filename = '{}.jpg'.format(data['date'])
        logging.info("Getting image data from {}".format(data['url']))
        response = requests.get(data['url'])
        _file = io.BytesIO(response.content)
        logging.info("Uploading media")
        media = tweepy_api.media_upload(filename=filename, file=_file)
        logging.info(media)
        logging.info("Creating tweet")
        tweepy_client.create_tweet(text=tweet, media_ids=[media.media_id_string])
        
    else:
        logging.info("Creating tweet")
        # tweepy_client.update_status(tweet)

def create_tweet(tweet):
    api = tw_manager.get_tweepy_client()
    api.create_tweet(text=tweet)