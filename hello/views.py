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
        try:
            longitude = float(request.POST.get("longitude", None))
            latitude = float(request.POST.get("latitude", None))
            total = longitude + latitude
            if total < 10:
                html = "<html><body>The total is less than 10.</body></html>"
                return HttpResponse(html)
            else:
                html = "<html><body>The total is 10 or more.</body></html>"
                return HttpResponse(html)
        except:
            html = "<html><body>There was some error.</body></html>"
            return HttpResponse(html)
    html = "<html><body>Nothing happened.</body></html>"
    return HttpResponse(html)
