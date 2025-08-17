from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-team/', views.create_team, name='create_team'),
    path('create-player/', views.create_player, name='create_player'),
    path('create-article/', views.create_article, name='create_article'),
    path('search/', views.search, name='search'),
]
