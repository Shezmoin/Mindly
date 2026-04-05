from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
        },
        {
            'title': 'Low Mood Recovery Toolkit',
            'category': 'Depression',
            'description': 'Small daily actions that can support energy, routine, and motivation during difficult periods.',
        },
        {
            'title': '5-Minute Grounding Practice',
            'category': 'Mindfulness',
            'description': 'A short guided exercise to reset your focus when your mind feels overwhelmed.',
        },
        {
            'title': 'Sleep Reset Checklist',
            'category': 'Sleep',
            'description': 'Simple bedtime habits to improve sleep quality and reduce next-day mental fatigue.',
        },
        {
            'title': 'Managing Daily Stress',
            'category': 'Stress',
            'description': 'A structured approach for identifying pressure points and planning calmer routines.',
        },
        {
            'title': 'Compassionate Self-Talk Guide',
            'category': 'Self-Care',
            'description': 'Learn how to replace harsh inner criticism with supportive language and realistic goals.',
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
