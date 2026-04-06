from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import JournalEntryForm, MoodEntryForm
from .models import JournalEntry, MoodEntry

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


@login_required
def mood_list_view(request):
    entries = MoodEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'journal/mood_list.html', {'entries': entries})


@login_required
def journal_create_view(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            journal_entry = form.save(commit=False)
            journal_entry.user = request.user
            journal_entry.save()
            messages.success(request, 'Journal entry saved successfully.')
            return redirect('journal:journal-list')
    else:
        form = JournalEntryForm()

    return render(request, 'journal/journal_form.html', {'form': form})


@login_required
def journal_list_view(request):
    entries = JournalEntry.objects.filter(user=request.user).order_by('-updated_at')
    return render(request, 'journal/journal_list.html', {'entries': entries})
