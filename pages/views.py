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


@login_required
def dashboard_view(request):
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'pages/dashboard.html', context)
