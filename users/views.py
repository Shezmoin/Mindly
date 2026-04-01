from django.shortcuts import render

# Create your views here.

def register_view(request):
    """
    Placeholder view for user registration.
    """
    return render(request, 'users/register.html')

def login_view(request):
    """
    Placeholder view for user login.
    """
    return render(request, 'users/login.html')

def profile_view(request):
    """
    Placeholder view for user profile.
    """
    return render(request, 'users/profile.html')

def logout_view(request):
    """
    Placeholder view for user logout.
    """
    return render(request, 'users/logout.html')
