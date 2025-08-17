from django.shortcuts import render, redirect
from .models import Team
from .forms import TeamForm, PlayerForm, ArticleForm, SearchForm

def home(request):
    from .models import Article
    articles = Article.objects.all().order_by('-date')
    return render(request, "blog/home.html", {"articles": articles})

def create_team(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "blog/create_team.html", {"form": form})

def create_player(request):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "blog/create_player.html", {"form": form})

def create_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "blog/create_article.html", {"form": form})

def search(request):
    results = []
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data["search_term"]
            results = Team.objects.filter(name__icontains=search_term)
    else:
        form = SearchForm()
    return render(request, "blog/search_results.html", {"form": form, "results": results})
