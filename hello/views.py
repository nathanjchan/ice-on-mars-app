from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import numpy as np
import pandas as pd

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()
    
    return render(request, "db.html", {"greetings": greetings})


def distance(x1, y1, x2, y2):
    return np.sqrt(np.sum((x1-x2)**2 + (y1-y2)**2))


def search(request):
    if request.method == "POST":
        longitude = float(request.POST.get("longitude", None))
        latitude = float(request.POST.get("latitude", None))

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
            depth_message = "<p>According to the model from Piqueux et al. 2019, there is no ice on this location.</p>"
        else:
            depth_message = "".join(["<p>According to the model from Piqueux et al. 2019, there is ice ", str(min_depth), " cm under the surface at this location.</p>"])

        html_list = [
            "<html><body><center>",
            "<p>Here is a radar image at {longitude: ", str(min_long), ", latitude: ", str(min_lat), "},</p>",
            "<p>which is ", str(min_dist), " units away from {longitude: ", str(longitude), ", latitude: ", str(latitude), "}.</p>",
            depth_message,
            "<p>The image is from the Geosciences Node of the NASA Planetary Data System.</p>"
            '<p><img src="', min_jpg, '" alt="radar image"></p>',
            "</center></body><html>"
        ]
        html = "".join(html_list)
        return HttpResponse(html)
    html = "<html><body>There was some error and nothing happened.</body></html>"
    return HttpResponse(html)
