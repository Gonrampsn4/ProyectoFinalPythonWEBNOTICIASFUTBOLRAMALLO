
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','avatar','link','birthday']
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control','rows':4}),
            'link': forms.URLInput(attrs={'class':'form-control'}),
            'birthday': forms.DateInput(attrs={'type':'date','class':'form-control'}),
        }
