from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import EventForm

# Create your views here.
from events.models import Event


def all_events(request):
    events_all = Event.objects.all().order_by('-date_published')
    paginator = Paginator(events_all, 10)

    page = request.GET.get('page')

    if hasattr(request.user, 'teacher') or hasattr(request.user, 'company'):
        perm_to_create = True
    else:
        perm_to_create = False

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page(paginator.num_pages)

    return render(request, 'events/all_events.html', {'events': events, 'perm_to_create': perm_to_create })


def event_page(request, pk):
    event = get_object_or_404(Event, pk=pk)
    subscribed = event.is_subscribed(request.user)
    return render(request, 'events/event_page.html', {'event': event, 'subscribed': subscribed})


def subscribe(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.subscribe(request.user)
    message = 'Thanks for subscribing!'
    return render(request, 'events/event_page.html', {'event': event, 'subscribed': True, 'message': message})


def create_new(request):
    if hasattr(request.user, 'teacher') or hasattr(request.user, 'company'):
        if request.method == "POST":
            form = EventForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.creator = request.user
                event.date_published = timezone.now()
                event.save()
                return redirect('events.views.event_page', pk=event.pk)
        else:
            form = EventForm()
        return render(request, 'events/edit_event_page.html', {'form': form})
    else:
        raise PermissionDenied()


def event_edit(request, pk):
    if hasattr(request.user, 'teacher') or hasattr(request.user, 'company'):
        event = get_object_or_404(Event, pk=pk)
        if request.method == "POST":
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                event = form.save(commit=False)
                event.creator = request.user
                event.date_published = timezone.now()
                event.save()
                return redirect('events.views.event_page', pk=event.pk)
        else:
            form = EventForm(instance=event)
            return render(request, 'events/edit_event_page.html', {'form': form})
    else:
        raise PermissionDenied()
