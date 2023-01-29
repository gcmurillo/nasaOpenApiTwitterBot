import os
import tweepy
import logging

class TweepyManager:

    def __init__(self):
        self.access_key = os.environ["ACCESS_KEY"]
        self.access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
        self.consumer_key = os.environ["CONSUMER_KEY"]
        self.consumer_key_secret = os.environ["CONSUMER_KEY_SECRET"]

    def get_tweepy_api(self):
        auth = tweepy.OAuth1UserHandler(
            self.consumer_key, self.consumer_key_secret,
            self.access_key, self.access_token_secret
        )
        return tweepy.API(auth)    
