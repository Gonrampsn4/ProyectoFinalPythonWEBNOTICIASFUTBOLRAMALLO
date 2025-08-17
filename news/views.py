
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import NewsArticle
from .forms import NewsArticleForm
from .mixins import AuthorRequiredMixin

class NewsListView(ListView):
    model = NewsArticle
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    paginate_by = 10

    

class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = 'news/news_detail.html'
    context_object_name = 'article'

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = NewsArticle
    form_class = NewsArticleForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

class NewsUpdateView(AuthorRequiredMixin, LoginRequiredMixin, UpdateView):
    model = NewsArticle
    form_class = NewsArticleForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news_list')

class NewsDeleteView(AuthorRequiredMixin, LoginRequiredMixin, DeleteView):
    model = NewsArticle
    template_name = 'news/news_confirm_delete.html'
    success_url = reverse_lazy('news_list')


from django.shortcuts import render

def home_view(request):
    qs = NewsArticle.objects.order_by('-published_at')
    headline = qs.first()
    secondary = qs[1:7]  # seis noticias secundarias
    return render(request, 'home.html', {'headline': headline, 'secondary': secondary})



def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['q'] = (self.request.GET.get('q') or '').strip()
    return ctx

