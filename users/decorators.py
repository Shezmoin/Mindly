from functools import wraps

from django.contrib import messages
from django.urls import reverse, NoReverseMatch
from django.shortcuts import redirect

from users.models import UserProfile


def premium_required(view_func):
    """Allow access only to users with a premium subscription tier."""

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)

        if profile.subscription_tier != UserProfile.TIER_PREMIUM:
            messages.info(request, 'Premium access required. Please upgrade to continue.')
            try:
                return redirect(reverse('pricing'))
            except NoReverseMatch:
                return redirect(reverse('payments:pricing'))

        return view_func(request, *args, **kwargs)

    return _wrapped_view
