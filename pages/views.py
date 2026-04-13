from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from users.decorators import premium_required
from users.models import UserProfile

# Create your views here.


def home_view(request):
    """
    Renders the homepage with welcome content and feature overview.

    Args:
        request: The HTTP request object

    Returns:
        Rendered home.html template
    """
    return render(request, 'pages/home.html')


def about_view(request):
    """
    Renders the about page with mission, values, and platform information.

    Args:
        request: The HTTP request object

    Returns:
        Rendered about.html template
    """
    return render(request, 'pages/about.html')


def resources_view(request):
    resources = [
        {
            'title': 'Understanding Anxiety Triggers',
            'category': 'Anxiety',
            'description': 'Practical ways to notice common triggers and respond before stress escalates.',
            'icon_emoji': '🧠',
        },
        {
            'title': 'Low Mood Recovery Toolkit',
            'category': 'Depression',
            'description': 'Small daily actions that can support energy, routine, and motivation during difficult periods.',
            'icon_emoji': '🌤️',
        },
        {
            'title': '5-Minute Grounding Practice',
            'category': 'Mindfulness',
            'description': 'A short guided exercise to reset your focus when your mind feels overwhelmed.',
            'icon_emoji': '🧘',
        },
        {
            'title': 'Sleep Reset Checklist',
            'category': 'Sleep',
            'description': 'Simple bedtime habits to improve sleep quality and reduce next-day mental fatigue.',
            'icon_emoji': '🌙',
        },
        {
            'title': 'Managing Daily Stress',
            'category': 'Stress',
            'description': 'A structured approach for identifying pressure points and planning calmer routines.',
            'icon_emoji': '🧩',
        },
        {
            'title': 'Compassionate Self-Talk Guide',
            'category': 'Self-Care',
            'description': 'Learn how to replace harsh inner criticism with supportive language and realistic goals.',
            'icon_emoji': '💚',
        },
    ]
    return render(request, 'pages/resources.html', {'resources': resources})


@login_required
def dashboard_view(request):
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'pages/dashboard.html', context)


@login_required
@premium_required
def premium_resources_view(request):
    return render(request, 'pages/premium_resources.html')
