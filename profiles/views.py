
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile.html', {'form': form, 'profile': profile})
