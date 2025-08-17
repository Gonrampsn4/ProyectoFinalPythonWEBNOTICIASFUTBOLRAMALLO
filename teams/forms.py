
from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name','league','league_fk','crest']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'league': forms.Select(attrs={'class':'form-select'}),
                'league_fk': forms.Select(attrs={'class':'form-select'}),
        }
