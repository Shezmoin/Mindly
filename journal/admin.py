from django.contrib import admin

from .models import JournalEntry, MoodEntry


@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'mood_score', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'is_private', 'created_at')
