from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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

class TicketUpdateView(UpdateView):
    """
    View to handle updating an existing ticket.
    Reuses the TicketForm and ticket_form.html template.
    """
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html' # Reusing the template!
    success_url = reverse_lazy('ticket_list')

class TicketDeleteView(DeleteView):
    """
    View to handle deleting an existing ticket.
    Asks for confirmation before removing the record from the database.
    """
    model = Ticket
    template_name = 'tickets/ticket_confirm_delete.html' # HTML for safety confirmation
    success_url = reverse_lazy('ticket_list') # Redirects back to list after deleting