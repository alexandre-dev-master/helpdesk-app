from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Ticket
from .forms import TicketForm

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        queryset = Ticket.objects.filter(user=self.request.user)
        
        status_filter = self.request.GET.get('status')
        
        if status_filter:
            queryset = queryset.filter(status=status_filter.upper())
            
        return queryset.order_by('-created_at')

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('ticket_list')

    def form_valid(self, form):
        """Automatically set the logged-in user as the author of the ticket."""
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TicketDetailView(LoginRequiredMixin, DetailView): 
    model = Ticket
    template_name = 'tickets/ticket_detail.html'
    context_object_name = 'ticket'


class TicketUpdateView(LoginRequiredMixin, UpdateView): 
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('ticket_list')


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    template_name = 'tickets/ticket_confirm_delete.html'
    success_url = reverse_lazy('ticket_list')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})