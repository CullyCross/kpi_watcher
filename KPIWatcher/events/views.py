from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from events.models import Event


def all_events(request):
    events_all = Event.objects.all().order_by('date_published')
    paginator = Paginator(events_all, 10)

    page = request.GET.get('page')

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page(paginator.num_pages)

    return render(request, 'events/all_events.html', {'events': events})


def event_page(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_page.html', {'event': event})



def subscribe(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.subscribe(request.user)
    return HttpResponseRedirect(reverse('event_page', kwargs={'pk': event.pk}))

