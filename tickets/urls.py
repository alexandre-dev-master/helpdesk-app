"""
URL routing configuration for the tickets application.
Maps web requests to the appropriate views.
"""

from django.urls import path
from .views import TicketListView, TicketCreateView, TicketDetailView

urlpatterns = [
    path('', TicketListView.as_view(), name='ticket_list'),
    path('new/', TicketCreateView.as_view(), name='ticket_create'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'), # Dinamic routing for ticket details
]