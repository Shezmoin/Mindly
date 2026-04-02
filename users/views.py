from django.contrib import auth
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('pages:home')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    """
    Placeholder view for user login.
    """
    return render(request, 'users/login.html')


def profile_view(request):
    """
    Placeholder view for user profile.
    """
    return render(request, 'users/profile.html')


def logout_view(request):
    """
    Placeholder view for user logout.
    """
    return render(request, 'users/logout.html')
