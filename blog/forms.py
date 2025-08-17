from django import forms
from .models import Team, Player, Article

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class SearchForm(forms.Form):
    search_term = forms.CharField(label='Buscar equipo', max_length=100)
