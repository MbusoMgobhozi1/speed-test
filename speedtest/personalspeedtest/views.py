import requests
import logging
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

log = logging.getLogger(__name__)

TEN_MB_URL = "https://link.testfile.org/PDF10MB"
FIFTY_MB_URL = "https://link.testfile.org/PDF50MB"
HUNDRED_MB_URL ="https://link.testfile.org/PDF100MB"
TOTAL_MB = 160

def index(request:HttpRequest) -> HttpResponse:
    """
    Function to render the index page.
    """
    return render(request, "index.html")

def speedtest(request:HttpRequest) -> JsonResponse:
    """
    Function to get the upload and download speeds of a user.
    """
    download_speeds = get_download_speeds()
    upload_speeds = get_upload_speeds()
    # ping = await get_ping()

    return JsonResponse({"download_speeds": download_speeds.get("download_speeds"), "upload_speeds": upload_speeds.get("upload_speeds")})

def get_download_speeds() -> dict:
    """
    Function tracks the time taken for a user to download a certain amount of data from a server.
    """
    start_time = datetime.now()
    requests.get(TEN_MB_URL)
    requests.get(FIFTY_MB_URL)
    requests.get(HUNDRED_MB_URL)
    end_time = datetime.now()

    megabytes_per_second = TOTAL_MB / (end_time - start_time).seconds
    return {"download_speeds": round(megabytes_per_second, 2)}

def get_upload_speeds() -> dict:
    """
    Function tracks the time taken for a user to upload a certain amount of data to a server.
    """
    return {"upload_speeds": 0.0}

def get_ping() -> dict:
    """
    Function to get the ping of a user.
    """
    return {"ping": 0}