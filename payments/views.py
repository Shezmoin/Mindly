from django.shortcuts import render

# Create your views here.

def index_view(request):
    """
    Placeholder view for payments index page.
    """
    return render(request, 'payments/index.html')
