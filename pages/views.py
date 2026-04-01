from django.shortcuts import render

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

