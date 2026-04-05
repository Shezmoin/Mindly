from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import MoodEntryForm

# Create your views here.


def index_view(request):
    """
    Placeholder view for journal index page.
    """
    return render(request, 'journal/index.html')


@login_required
def mood_create_view(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user
            mood_entry.save()
            messages.success(request, 'Mood entry saved successfully.')
            return redirect('pages:dashboard')
    else:
        form = MoodEntryForm()

    return render(request, 'journal/mood_form.html', {'form': form})
