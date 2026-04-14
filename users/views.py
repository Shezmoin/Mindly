from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import UserProfileEditForm, UserRegistrationForm



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
def profile_view(request):
    return render(request, 'users/profile.html')


@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('users:profile')
    else:
        form = UserProfileEditForm(instance=request.user)

    return render(request, 'users/profile_edit.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, 'You have been logged out successfully.')
    return render(request, 'users/logout.html')
