from django import forms

from .models import JournalEntry, MoodEntry


class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ('mood_score', 'note')
        widgets = {
            'mood_score': forms.NumberInput(
                attrs={
                    'type': 'range',
                    'min': 1,
                    'max': 10,
                    'step': 1,
                    'class': 'form-range',
                    'id': 'id_mood_score',
                }
            ),
            'note': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Add a note about how you are feeling (optional).',
                }
            ),
        }


class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ('title', 'content', 'is_private')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Give your entry a short title',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 8,
                    'placeholder': 'Write your thoughts here...',
                }
            ),
        }
