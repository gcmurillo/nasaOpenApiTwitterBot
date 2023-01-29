from tweepy_manager import TweepyManager
import logging
import requests
import io

tw_manager = TweepyManager()

def create_APOD_tweet(data):
    tweepy_client = tw_manager.get_tweepy_api()
    tweet = "Date: {0}\nTitle: {1}\nUrl: {2}\n#APOD #NASA @NASA".format(
        data['date'], data['title'], data['url'])
    if data['media_type'] == 'image':
        filename = '{}.jpg'.format(data['date'])
        logging.info("Getting image data from {}".format(data['url']))
        response = requests.get(data['url'])
        _file = io.BytesIO(response.content)
        logging.info("Creating tweet")
        tweepy_client.update_status_with_media(tweet, filename, file=_file)
    else:
        logging.info("Creating tweet")
        tweepy_client.update_status(tweet)
