
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import NewsArticle
from teams.models import Team

class NewsArticleForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    teams = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class':'form-select'})
    )
    class Meta:
        model = NewsArticle
        fields = ['title','subtitle','summary','body','image','teams']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'summary': forms.Textarea(attrs={'class':'form-control','rows':3}),
        }
