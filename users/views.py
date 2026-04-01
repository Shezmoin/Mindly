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
