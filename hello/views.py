from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .models import Greeting

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
        longitude = request.POST.get("longitude", None)
        latitude = request.POST.get("latitude", None)
        total = longitude + latitude
        if total < 10:
            messages.info(request, "Your search button worked, and the total is less than 10.")
            return render(request, "index.html")
        elif total >= 10:
            messages.info(request, "Your search button worked, and the total is 10 or more.")
            return render(request, "index.html")
        else:
            messages.info(request, "Your search button worked, but there was no total.")
            return render(request, "index.html")
    return render(request, "index.html")
