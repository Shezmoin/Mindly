<<<<<<< HEAD
from django.contrib import admin

from .models import JournalEntry, MoodEntry


@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
	list_display = ('user', 'mood_score', 'created_at')
	list_filter = ('mood_score', 'created_at')
	search_fields = ('user__username', 'note')


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
	list_display = ('title', 'user', 'is_private', 'created_at', 'updated_at')
	list_filter = ('is_private', 'created_at', 'updated_at')
	search_fields = ('title', 'content', 'user__username')
=======
# Register your models here.
>>>>>>> 04c11c74a48edb4abaea6dc8325a8cb21860f238
