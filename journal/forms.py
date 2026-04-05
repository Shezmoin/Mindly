from django import forms

from .models import MoodEntry


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
