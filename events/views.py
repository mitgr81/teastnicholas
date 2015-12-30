from django.shortcuts import render, get_object_or_404

from .models import Event


def index(request):
    upcoming_event_list = Event.objects.order_by('-start_date')[:5]

    context = {
        'upcoming_event_list': upcoming_event_list,
    }
    return render(request, 'events/index.html', context)


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', {'event': event})
