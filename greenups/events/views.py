from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from models import Event

class EventIndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'latest_event_list'

    def get_queryset(self):
        """Return the last five published events."""
        return Event.objects.order_by('-start_time')[:5]


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

