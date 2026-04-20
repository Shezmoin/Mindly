from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import UserProfileEditForm, UserRegistrationForm
from .models import UserProfile


def register_view(request):
    """Register a new user account and sign the user in."""
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
    """Authenticate a user and redirect to the requested destination."""
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
    """Render the logged-in user's profile page."""
    return render(request, 'users/profile.html')


@login_required
def profile_edit_view(request):
    """Update profile fields for the logged-in user."""
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('users:profile')
    else:
        form = UserProfileEditForm(instance=request.user)

    return render(request, 'users/profile_edit.html', {'form': form})


@login_required
def cancel_premium_view(request):
    """Downgrade a premium user back to the free subscription tier."""
    if request.method != 'POST':
        return redirect('users:profile')

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if profile.subscription_tier != UserProfile.TIER_PREMIUM:
        messages.info(request, 'Your account is already on the free plan.')
        return redirect('users:profile')

    profile.subscription_tier = UserProfile.TIER_FREE
    profile.save(update_fields=['subscription_tier'])

    messages.success(
        request,
        'Premium cancellation is being processed. Sorry to see you go. '
        'You can join back any time and continue using free content.',
    )
    return redirect('pages:home')


def logout_view(request):
    """Log out the current user and render the logout confirmation page."""
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, 'You have been logged out successfully.')
    return render(request, 'users/logout.html')
