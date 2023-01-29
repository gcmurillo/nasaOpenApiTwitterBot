import azure.functions as func
from nasa_api_manager import NasaApiManager
import utils

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
