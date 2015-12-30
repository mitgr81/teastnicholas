from django.shortcuts import render
from django.http import HttpResponse

from .models import Event


def index(request):
    upcoming_event_list = Event.objects.order_by('-start_date')[:5]

    context = {
        'upcoming_event_list': upcoming_event_list,
    }
    return render(request, 'events/index.html', context)


def detail(request, event_id):
    return HttpResponse("You're looking at event %s." % event_id)
