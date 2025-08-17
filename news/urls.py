
from django.urls import path
from .views import (
    NewsListView, NewsDetailView,
    NewsCreateView, NewsUpdateView, NewsDeleteView
)

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('crear/', NewsCreateView.as_view(), name='news_create'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('<slug:slug>/editar/', NewsUpdateView.as_view(), name='news_update'),
    path('<slug:slug>/borrar/', NewsDeleteView.as_view(), name='news_delete'),
]
