"""
URL routing configuration for the tickets application.
Maps web requests to the appropriate views.
"""

from django.urls import path
from .views import TicketListView, TicketCreateView, TicketDetailView, TicketUpdateView, TicketDeleteView

urlpatterns = [
    path('', TicketListView.as_view(), name='ticket_list'),
    path('new/', TicketCreateView.as_view(), name='ticket_create'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'), 
    path('<int:pk>/edit/', TicketUpdateView.as_view(), name='ticket_update'),
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
]