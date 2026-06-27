from django.views.generic import ListView, CreateView
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
    """
    View to handle the creation of a new ticket.
    Renders the form and saves valid data to the database.
    """
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    
    # Redirects the user back to the list view after successfully submitting the form
    success_url = reverse_lazy('ticket_list')