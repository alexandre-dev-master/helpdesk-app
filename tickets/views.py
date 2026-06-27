from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Ticket
from .forms import TicketForm

class TicketListView(ListView):
    """View to list all technical support tickets."""
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'
    ordering = ['-created_at']

class TicketCreateView(CreateView):
    """View to handle the creation of a new ticket."""
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('ticket_list')

class TicketDetailView(DetailView):
    """
    View to display the full details of a single ticket.
    Automatically fetches the object based on the ID passed via URL.
    """
    model = Ticket
    template_name = 'tickets/ticket_detail.html'
    context_object_name = 'ticket' # Singular form for a single object