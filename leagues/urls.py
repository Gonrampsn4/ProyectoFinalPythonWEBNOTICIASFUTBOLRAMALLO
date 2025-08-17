
from django.urls import path
from .views import LeagueListView, LeagueCreateView, LeagueUpdateView, LeagueDeleteView

urlpatterns = [
    path('', LeagueListView.as_view(), name='league_list'),
    path('crear/', LeagueCreateView.as_view(), name='league_create'),
    path('<int:pk>/editar/', LeagueUpdateView.as_view(), name='league_update'),
    path('<int:pk>/borrar/', LeagueDeleteView.as_view(), name='league_delete'),
]
