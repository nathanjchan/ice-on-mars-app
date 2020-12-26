from django.shortcuts import render
from django.http import HttpResponse

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
        total = int(longitude + latitude)
        if total < 10:
            html = "<html><body>Your search button worked, and the total is less than 10.</body></html>"
            return HttpResponse(html)
        elif total >= 10:
            html = "<html><body>Your search button worked, and the total is 10 or more.</body></html>"
            return HttpResponse(html)
        else:
            html = "<html><body>Your search button worked, but there was no total.</body></html>"
            return HttpResponse(html)
    html = "<html><body>Your search button worked, but nothing happened.</body></html>"
    return HttpResponse(html)
