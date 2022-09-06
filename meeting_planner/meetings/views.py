from django.shortcuts import render, get_object_or_404
from .models import Meeting, Room
from django.forms import modelform_factory

def detail(request, id):
    #meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id )
    return render(request, "meetings/detail.html",
                  {"meeting": meeting}
                  )

def rooms(request):
    rooms = Room.objects.all()
    return render(request, "meetings/rooms.html",
                   {"rooms": rooms}
                   )


# please add a new page that shows a list of all room objects
# ( just text, no link)

# create a:
# - view
# - template
# - url mapping


MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})

