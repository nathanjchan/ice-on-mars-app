from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Greeting

import numpy as np
import pandas as pd
from .utilities import distance

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()
    
    return render(request, "db.html", {"greetings": greetings})


def search(request):
    if request.method == "POST":
        longitude = int(request.POST.get("longitudeSlider", None))
        latitude = int(request.POST.get("latitudeSlider", None))

        df = pd.read_csv("https://github.com/nathanjchan/ice-on-mars/raw/master/radar2.csv")
        df = df.drop(columns="Unnamed: 0")

        min_dist = float("inf")
        min_tif = ""
        min_depth = 0
        min_long = 0
        min_lat = 0
        for index, row in df.iterrows():
            dist = distance(longitude, latitude, row["center_long"], row["center_lat"])
            if dist < min_dist:
                min_dist = dist
                min_tif = row["tif"]
                min_depth = row["depth"]

                min_long = row["center_long"]
                min_lat = row["center_lat"]

                min_tif = min_tif.split("Radar_Images/tiff/")[1]
                min_tif = min_tif.split("tiff.tif")[0]
                min_jpg = "".join(["https://pds-geosciences.wustl.edu/mro/mro-m-sharad-5-radargram-v1/mrosh_2001/browse/thm/", min_tif, "thm.jpg"])

        if min_depth == -32768:
            depth_message = '<p>According to the model from <a href="https://doi.org/10.1029/2019GL083947">Piqueux et al. 2019</a>, <b>there is no ice on this location</b>.</p>'
        else:
            depth_message = "".join(['<p>According to the model from <a href="https://doi.org/10.1029/2019GL083947">Piqueux et al. 2019</a>, <b>there is ice ', str(min_depth), " cm under the surface at this location</b>.</p>"])

        html_list = [
            "<html><body>",
            "<style> h1 {text-align: center;} h2 {text-align: center;} p {text-align: center;} </style>"
            '<img src="https://ice-on-mars.herokuapp.com/static/mars.jpg" alt="mars" height="100">',
            "<h1>Ice on Mars</h1>",
            "<h2>Finding near-surface ice on Mars from radar images</h2>"
            "<p>Here is a SHARAD radar image at {longitude: ", str(min_long), ", latitude: ", str(min_lat), "},</p>",
            "<p>which is ", str(round(min_dist, 2)), " units away from the requested coordinates {longitude: ", str(longitude), ", latitude: ", str(latitude), "}.</p>",
            depth_message,
            '<p>The image is from the <a href="https://pds-geosciences.wustl.edu/">Geosciences Node of the NASA Planetary Data System</a>.</p>',
            '<p><a href="https://ice-on-mars.herokuapp.com/">Home</a></p>',
            '<p><img src="', min_jpg, '" alt="radar image" height="900"></p>',
            "</body><html>",
        ]
        html = "".join(html_list)
        return HttpResponse(html)
    else:
        return redirect("index")
