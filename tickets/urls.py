"""
URL routing configuration for the tickets application.
Maps web requests to the appropriate views.
"""
from django.urls import path
from .views import TicketListView

urlpatterns = [ 
    path('', TicketListView.as_view(), name='ticket_list'),
]