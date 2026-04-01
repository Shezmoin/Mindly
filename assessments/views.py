from django.shortcuts import render

# Create your views here.


def index_view(request):
    """
    Placeholder view for assessments index page.
    """
    return render(request, 'assessments/index.html')
