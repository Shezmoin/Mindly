import logging

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import (
    PasswordResetConfirmView as DjangoPasswordResetConfirmView,
    PasswordResetView as DjangoPasswordResetView,
)
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import UserProfileEditForm, UserRegistrationForm
from .models import CustomUser, UserProfile


logger = logging.getLogger(__name__)


def register_view(request):
    """Register a new user account and sign the user in."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            messages.success(
                request,
                'You have successfully registered to Mindly.',
                extra_tags='persist',
            )
            return redirect('users:register-success')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def register_success_view(request):
    """Render a post-registration success page with key navigation actions."""
    return render(request, 'users/register_success.html')


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


@login_required
@require_POST
def logout_view(request):
    """Log out the current user and render the logout confirmation page."""
    auth.logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return render(request, 'users/logout.html')


class PasswordResetView(DjangoPasswordResetView):
    """Custom password reset view that captures username for recovery."""
    
    template_name = 'users/password_reset.html'
    success_url = '/users/password-reset/done/'
    
    def form_valid(self, form):
        """Store the username in session for the done template to display."""
        email = form.cleaned_data['email']
        user = CustomUser.objects.filter(email=email).only('username').first()
        if user is not None:
            # Store username and email in session for done template
            self.request.session['reset_username'] = user.username
            self.request.session['reset_email'] = email

        try:
            return super().form_valid(form)
        except Exception:
            logger.exception('Password reset email failed for %s', email)
            return redirect(self.success_url)


class PasswordResetConfirmView(DjangoPasswordResetConfirmView):
    """Custom password reset confirm view that redirects to the Mindly completion page."""

    template_name = 'users/password_reset_confirm.html'
    success_url = '/users/password-reset/complete/'
