from django.db import models

class Ticket(models.Model):
    """
    Represents a technical support ticket within the helpdesk system.
    Stores information about the issue, its current status, and priority level.
    """
    
    # Status options using standard Django choices tuple
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    # Priority options to determine urgency
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a readable string representation of the ticket."""
        return f"[{self.priority.upper()}] {self.title}"