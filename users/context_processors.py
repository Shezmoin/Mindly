from users.models import UserProfile


def subscription_status(request):
    """Expose subscription tier flags to templates safely."""
    is_premium_user = False
    user_subscription_tier = None

    if request.user.is_authenticated:
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        user_subscription_tier = profile.subscription_tier
        is_premium_user = user_subscription_tier == UserProfile.TIER_PREMIUM

    return {
        'is_premium_user': is_premium_user,
        'user_subscription_tier': user_subscription_tier,
    }
