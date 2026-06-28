from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm # Importa o formulário de cadastro padrão
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Ticket
from .forms import TicketForm

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        # 1. Start by getting only the current user's tickets
        queryset = Ticket.objects.filter(user=self.request.user)
        
        # 2. Catch the 'status' parameter from the URL (e.g., /?status=open)
        status_filter = self.request.GET.get('status')
        
        # 3. If there is a filter, apply it to the database search
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

# Adicione esta função simples no final do seu arquivo views.py
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Salva o novo usuário no banco de dados
            return redirect('login') # Manda direto para a tela de login
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})