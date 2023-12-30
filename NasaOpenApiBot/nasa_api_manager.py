import requests
import os
import logging
import json

class ApodResponse(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

class ApodResponseList(object):
    items = []
    def __init__(self, j):
        _items = json.loads(j)
        for i in _items:
            self.items.append(i)


class NasaApiManager:

    def __init__(self):
        self.api_key = os.environ["NASA_API_KEY"]

    def get_apod_image(self):
        logging.info("Getting APOD image")
        response = requests.get(
            "https://api.nasa.gov/planetary/apod?api_key={0}".format(self.api_key))
        apod_response = ApodResponse(response.content)
        return apod_response
    
    def get_random_pictures(self, count = 100):
        logging.info("Getting random pictures {}".format(count))
        response = requests.get(
            "https://api.nasa.gov/planetary/apod?api_key={0}&count={1}".format(
                self.api_key,
                count
                )
        )
        apod_response = ApodResponseList(response.text)
        return apod_response
