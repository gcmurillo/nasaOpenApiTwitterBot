import azure.functions as func
from nasa_api_manager import NasaApiManager
import utils
import json
import random

app = func.FunctionApp()
api_manager = NasaApiManager()

@app.function_name(name="PictureOfTheDay")
@app.route(route="apod") # HTTP Trigger
def picture_of_the_day(req: func.HttpRequest) -> func.HttpResponse:
    res = api_manager.get_apod_image().__dict__
    utils.create_APOD_tweet(res)
    return func.HttpResponse("APOD request processed!!!")


@app.function_name(name="RandomPictures")
@app.route(route="random-picture")
def random_picture(req: func.HttpRequest) -> func.HttpResponse:
    res = api_manager.get_random_pictures().items[0]
    utils.create_APOD_tweet(res)
    return func.HttpResponse("Random Picture processed!")


@app.function_name(name="RandomPicturesTimeTrigger")
@app.schedule(schedule="0 */10 * * * *",
              arg_name="mytimer",
              run_on_startup=True)
def random_pictures_time_trigger(mytimer: func.TimerRequest) -> None:
    res = random.choice(api_manager.get_random_pictures().items)
    utils.create_APOD_tweet(res)

@app.function_name(name="createTweet")
@app.route(route="tweet")
def tweet(req: func.HttpRequest) -> func.HttpResponse:
    body = json.loads(req.get_body().decode('utf-8'))
    utils.create_tweet(body["text"])
    return func.HttpResponse("Tweet created!")
