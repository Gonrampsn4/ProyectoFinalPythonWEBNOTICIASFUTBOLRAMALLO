
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import League
from .forms import LeagueForm

class LeagueListView(ListView):
    model = League
    template_name = 'leagues/league_list.html'
    context_object_name = 'leagues'

class LeagueCreateView(LoginRequiredMixin, CreateView):
    model = League
    form_class = LeagueForm
    template_name = 'leagues/league_form.html'
    success_url = reverse_lazy('league_list')

class LeagueUpdateView(LoginRequiredMixin, UpdateView):
    model = League
    form_class = LeagueForm
    template_name = 'leagues/league_form.html'
    success_url = reverse_lazy('league_list')

class LeagueDeleteView(LoginRequiredMixin, DeleteView):
    model = League
    template_name = 'leagues/league_confirm_delete.html'
    success_url = reverse_lazy('league_list')
