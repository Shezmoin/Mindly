from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import JournalEntryForm, MoodEntryForm
from .models import JournalEntry, MoodEntry


@login_required
def mood_delete_view(request, pk):
    """Delete a selected mood entry for the logged-in user."""
    mood_entry = get_object_or_404(MoodEntry, pk=pk, user=request.user)

    if request.method == 'POST':
        mood_entry.delete()
        messages.success(request, 'Mood entry deleted successfully.')
        return redirect('journal:mood-list')

    return render(
        request,
        'journal/mood_confirm_delete.html',
        {'entry': mood_entry},
    )

# View definitions


def index_view(request):
    """Render the Journal Hub overview page."""
    return render(request, 'journal/index.html')


@login_required
def mood_create_view(request):
    """Create a new mood entry for the current user."""
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
def mood_edit_view(request, pk):
    """Edit a mood entry owned by the current user."""
    mood_entry = get_object_or_404(MoodEntry, pk=pk, user=request.user)

    if request.method == 'POST':
        form = MoodEntryForm(request.POST, instance=mood_entry)
        if form.is_valid():
            updated_entry = form.save(commit=False)
            updated_entry.user = request.user
            updated_entry.save()
            messages.success(request, 'Mood entry updated successfully.')
            return redirect('journal:mood-list')
    else:
        form = MoodEntryForm(instance=mood_entry)

    return render(
        request,
        'journal/mood_form.html',
        {
            'form': form,
            'is_edit': True,
            'entry': mood_entry,
        },
    )


@login_required
def mood_list_view(request):
    """List mood entries for the current user."""
    entries = MoodEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'journal/mood_list.html', {'entries': entries})


@login_required
def journal_create_view(request):
    """Create a journal entry while enforcing free-tier monthly limits."""
    user_profile = getattr(request.user, 'profile', None)
    is_free = getattr(user_profile, 'subscription_tier', 'free') == 'free'

    now = datetime.now()
    current_month_entries = JournalEntry.objects.filter(
        user=request.user,
        created_at__year=now.year,
        created_at__month=now.month,
    ).count()

    if is_free and current_month_entries >= 5:
        messages.error(
            request,
            'Free users can only create 5 journal entries per month. '
            'Upgrade to Premium for unlimited entries!',
        )
        return redirect('journal:journal-list')

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
    """List journal entries for the current user with title filtering."""
    query = request.GET.get('q', '')
    entries = JournalEntry.objects.filter(
        user=request.user,
        title__icontains=query,
    ).order_by('-updated_at')
    return render(request, 'journal/journal_list.html', {'entries': entries})


@login_required
def journal_detail_view(request, pk):
    """Render a single journal entry owned by the current user."""
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    return render(request, 'journal/journal_detail.html', {'entry': entry})


@login_required
def journal_edit_view(request, pk):
    """Edit an existing journal entry owned by the current user."""
    journal_entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)

    if request.method == 'POST':
        form = JournalEntryForm(request.POST, instance=journal_entry)
        if form.is_valid():
            updated_entry = form.save(commit=False)
            updated_entry.user = request.user
            updated_entry.save()
            messages.success(request, 'Journal entry updated successfully.')
            return redirect('journal:journal-list')
    else:
        form = JournalEntryForm(instance=journal_entry)

    return render(
        request,
        'journal/journal_form.html',
        {
            'form': form,
            'is_edit': True,
            'entry': journal_entry,
        },
    )


@login_required
def journal_delete_view(request, pk):
    """Delete a journal entry owned by the current user."""
    journal_entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)

    if request.method == 'POST':
        journal_entry.delete()
        messages.success(request, 'Journal entry deleted successfully.')
        return redirect('journal:journal-list')

    return render(
        request,
        'journal/journal_confirm_delete.html',
        {'entry': journal_entry},
    )
