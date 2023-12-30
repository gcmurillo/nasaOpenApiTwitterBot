import os
import tweepy
import logging

class TweepyManager:

    def __init__(self):
        self.bearer = os.environ["BEARER_TWITTER"]
        self.api_key = os.environ["API_KEY"]
        self.api_secret_key = os.environ["API_SECRET_KEY"]
        self.access_token = os.environ["ACCESS_TOKEN"]
        self.access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

    def get_tweepy_client(self):
        return tweepy.Client(consumer_key=self.api_key, consumer_secret=self.api_secret_key,
                             access_token=self.access_token, access_token_secret=self.access_token_secret)
    
    def get_tweepy_api_1(self):
        auth = tweepy.OAuth1UserHandler(
            self.api_key, self.api_secret_key,
            self.access_token, self.access_token_secret
        )
        return tweepy.API(auth=auth)
