from django.views.generic import ListView
from .models import Event


class EventPageView(ListView):
    model = Event
    template_name = 'events.html'
