from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from users.decorators import premium_required
from users.models import UserProfile

# View definitions


def home_view(request):
    """Render the homepage with core Mindly highlights."""
    return render(request, 'pages/home.html')


def about_view(request):
    """Render the about page with mission and platform information."""
    return render(request, 'pages/about.html')


def resources_view(request):
    """Render free and premium resource cards with user access flags."""
    resources = [
        {
            'title': 'Understanding Anxiety Triggers',
            'category': 'Anxiety',
            'description': (
                'Practical ways to notice common triggers and respond '
                'before stress escalates.'
            ),
            'is_premium': False,
            'url_name': 'pages:resource-anxiety',
        },
        {
            'title': 'Low Mood Recovery Toolkit',
            'category': 'Depression',
            'description': (
                'Small daily actions that can support energy, routine, '
                'and motivation during difficult periods.'
            ),
            'is_premium': False,
            'url_name': 'pages:resource-depression',
        },
        {
            'title': '5-Minute Grounding Practice',
            'category': 'Mindfulness',
            'description': (
                'A short guided exercise to reset your focus when your '
                'mind feels overwhelmed.'
            ),
            'is_premium': True,
            'url_name': 'pages:resource-mindfulness',
        },
        {
            'title': 'Sleep Reset Checklist',
            'category': 'Sleep',
            'description': (
                'Simple bedtime habits to improve sleep quality and '
                'reduce next-day mental fatigue.'
            ),
            'is_premium': True,
            'url_name': 'pages:resource-sleep',
        },
        {
            'title': 'Managing Daily Stress',
            'category': 'Stress',
            'description': (
                'A structured approach for identifying pressure points '
                'and planning calmer routines.'
            ),
            'is_premium': False,
            'url_name': 'pages:resource-stress',
        },
        {
            'title': 'Compassionate Self-Talk Guide',
            'category': 'Self-Care',
            'description': (
                'Learn how to replace harsh inner criticism with '
                'supportive language and realistic goals.'
            ),
            'is_premium': True,
            'url_name': 'pages:resource-selfcare',
        },
    ]
    user_profile = getattr(request.user, 'profile', None)
    is_premium = (
        getattr(user_profile, 'subscription_tier', 'free') == 'premium'
        if request.user.is_authenticated
        else False
    )
    return render(
        request,
        'pages/resources.html',
        {'resources': resources, 'is_premium': is_premium},
    )


def resource_anxiety_view(request):
    """Render the anxiety resource detail page."""
    return render(request, 'pages/resources/anxiety.html')


def resource_depression_view(request):
    """Render the depression resource detail page."""
    return render(request, 'pages/resources/depression.html')


@login_required
@premium_required
def resource_mindfulness_view(request):
    """Render the premium mindfulness resource detail page."""
    return render(request, 'pages/resources/mindfulness.html')


@login_required
@premium_required
def resource_sleep_view(request):
    """Render the premium sleep resource detail page."""
    return render(request, 'pages/resources/sleep.html')


def resource_stress_view(request):
    """Render the stress resource detail page."""
    return render(request, 'pages/resources/stress.html')


@login_required
@premium_required
def resource_selfcare_view(request):
    """Render the premium self-care resource detail page."""
    return render(request, 'pages/resources/selfcare.html')


@login_required
def dashboard_view(request):
    """Render the authenticated user dashboard with profile context."""
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'pages/dashboard.html', context)


@login_required
@premium_required
def premium_resources_view(request):
    """Render the premium-only resources landing page."""
    return render(request, 'pages/premium_resources.html')
