from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
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
    next_url = request.GET.get('next') or request.POST.get('next') or 'pages:home'

<<<<<<< HEAD
    if request.user.is_authenticated:
        return redirect(next_url)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            messages.success(request, 'Welcome back! You are now logged in.')
            return redirect(next_url)
    else:
        form = AuthenticationForm(request)

    return render(request, 'users/login.html', {'form': form, 'next': next_url})


@login_required
=======

>>>>>>> 04c11c74a48edb4abaea6dc8325a8cb21860f238
def profile_view(request):
    return render(request, 'users/profile.html')


def logout_view(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, 'You have been logged out successfully.')
    return render(request, 'users/logout.html')
