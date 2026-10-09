from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm


def index(request):

    # =========================
    # HANDLE POST REQUESTS
    # =========================

    if request.method == 'POST':

        action = request.POST.get('action')


        # =========================
        # ADD EVENT
        # =========================

        if action == 'add':

            form = EventForm(request.POST)

            if form.is_valid():
                form.save()

            return redirect('dashboard')


        # =========================
        # EDIT EVENT
        # =========================

        elif action == 'edit':

            event_id = request.POST.get('event_id')

            event = get_object_or_404(
                Event,
                event_id=event_id
            )

            form = EventForm(
                request.POST,
                instance=event
            )

            if form.is_valid():
                form.save()

            return redirect('dashboard')


        # =========================
        # DELETE EVENT
        # =========================

        elif action == 'delete':

            event_id = request.POST.get('event_id')

            event = get_object_or_404(
                Event,
                event_id=event_id
            )

            event.delete()

            return redirect('dashboard')


    # =========================
    # GET ALL EVENTS
    # =========================

    events = Event.objects.all().order_by(
        'date',
        'time'
    )


    # =========================
    # UPCOMING EVENTS
    # =========================
    # Counts all events whose
    # status is "Upcoming"

    upcoming_events_count = Event.objects.filter(
        status='Upcoming'
    ).count()


    # =========================
    # FORM
    # =========================

    form = EventForm()


    # =========================
    # CONTEXT
    # =========================

    context = {
        'events': events,
        'form': form,
        'upcoming_events_count': upcoming_events_count,
    }


    # =========================
    # RENDER DASHBOARD
    # =========================

    return render(
        request,
        'Inv_Events/dashboard.html',
        context
    )