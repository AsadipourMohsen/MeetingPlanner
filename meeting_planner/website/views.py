import random
from datetime import datetime

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from meetings.models import Meeting


def welcome(request):
    # the path argument should match the path of the file relative to template folder
    return render(request,
                  "website/welcome.html",
                  {"message": "this data was send from the view to the template",
                   "x": "1",
                   "age": 33,
                   "meetings": Meeting.objects.all()
                   }

                  )


def date(request):
    return HttpResponse("this page was served at: " + str(datetime.now()))


#please add an about page that shows some text about yourselfe

def about(request):
    return HttpResponse("Royce, he is a bad ass programmer who can make " + str(random.randint(1, 12 )) + " Million in the" + str(datetime.now()))