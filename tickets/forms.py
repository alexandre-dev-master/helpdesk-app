"""
Forms configuration for the tickets application.
Handles user input validation for creating and updating support tickets.
"""

from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    """
    Form mapped directly to the Ticket model.
    Automatically generates fields and handles validation.
    """
    class Meta:
        model = Ticket
        # We only expose fields that the user should fill
        fields = ['title', 'description', 'priority']
        
        # Adding HTML attributes to style fields nicely later
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter a concise title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe the technical issue in detail', 'rows': 4}),
            'priority': forms.Select(),
        }