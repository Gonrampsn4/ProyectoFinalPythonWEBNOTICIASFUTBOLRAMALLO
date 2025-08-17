
from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('crear/', PageCreateView.as_view(), name='page_create'),
    path('<slug:slug>/', PageDetailView.as_view(), name='page_detail'),
    path('<slug:slug>/editar/', PageUpdateView.as_view(), name='page_update'),
    path('<slug:slug>/borrar/', PageDeleteView.as_view(), name='page_delete'),
]
