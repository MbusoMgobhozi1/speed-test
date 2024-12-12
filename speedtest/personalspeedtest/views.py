from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request:HttpRequest) -> HttpResponse:
    return HttpResponse("index.html")

def speedtest(request:HttpRequest) -> dict:
    # define functions for fetching upload and download speeds
    # first return the dictionary with speed results
    # each return the result in a dictionary with the key being the speed type
    return {}

async def get_download_speed() -> dict:
    # function should track the time taken for a download to occur however based on size
    # starting at 10 MB to 100 MB
    return {}