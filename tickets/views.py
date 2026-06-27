from django.views.generic import ListView
from .models import Ticket

class TicketListView(ListView):
    """
    View to list all technical support tickets.
    Renders the public dashboard for tracking issues.
    """
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'
    
    # Ordering tickets so the newest ones appear first
    ordering = ['-created_at']