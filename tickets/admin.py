from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """
    Configuration for the Ticket model in the Django admin interface.
    Defines displayed fields, filters, and search capabilities.
    """
    
    # Fields to display in the list view table
    list_display = ('title', 'status', 'priority', 'created_at')
    
    # Sidebar filters to easily sort through tickets
    list_filter = ('status', 'priority', 'created_at')
    
    # Search bar config to find tickets by title or description
    search_fields = ('title', 'description')