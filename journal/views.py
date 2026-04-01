from django.shortcuts import render

# Create your views here.


def index_view(request):
    """
    Placeholder view for journal index page.
    """
    return render(request, 'journal/index.html')
