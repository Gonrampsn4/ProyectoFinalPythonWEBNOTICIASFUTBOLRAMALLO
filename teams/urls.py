
from django.urls import path
from .views import TeamListView, TeamCreateView, TeamUpdateView, TeamDeleteView

urlpatterns = [
    path('', TeamListView.as_view(), name='team_list'),
    path('crear/', TeamCreateView.as_view(), name='team_create'),
    path('<int:pk>/editar/', TeamUpdateView.as_view(), name='team_update'),
    path('<int:pk>/borrar/', TeamDeleteView.as_view(), name='team_delete'),
]
