from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Event
from .forms import EventForm


def get_context(active_page):
    events = Event.objects.all().order_by('date', 'time')

    upcoming_events_count = events.filter(
        date__gte=timezone.localdate(),
        status='Upcoming'
    ).count()

    return {
        'events': events,
        'form': EventForm(),
        'active_page': active_page,
        'upcoming_events_count': upcoming_events_count,
    }


def index(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            form = EventForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('dashboard')

        elif action == 'edit':
            event_id = request.POST.get('event_id')
            event = get_object_or_404(Event, pk=event_id)
            form = EventForm(request.POST, instance=event)

            if form.is_valid():
                form.save()
                return redirect('dashboard')

        elif action == 'delete':
            event_id = request.POST.get('event_id')
            event = get_object_or_404(Event, pk=event_id)
            event.delete()
            return redirect('dashboard')

    context = get_context('dashboard')
    return render(request, 'Inv_Events/dashboard.html', context)


def events_page(request):
    context = get_context('events')
    return render(request, 'Inv_Events/dashboard.html', context)


def participants_page(request):
    context = get_context('participants')
    return render(request, 'Inv_Events/dashboard.html', context)


def settings_page(request):
    context = get_context('settings')
    return render(request, 'Inv_Events/dashboard.html', context)
