from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class AssessmentResult(models.Model):
    ASSESSMENT_MOOD = 'mood'
    ASSESSMENT_STRESS = 'stress'
    ASSESSMENT_SLEEP = 'sleep'
    ASSESSMENT_CHOICES = [
        (ASSESSMENT_MOOD, 'Mood Self-Check'),
        (ASSESSMENT_STRESS, 'Stress Self-Check'),
        (ASSESSMENT_SLEEP, 'Sleep Habits Check'),
    ]

    LEVEL_LOW = 'Low concern'
    LEVEL_MODERATE = 'Moderate concern'
    LEVEL_HIGHER = 'Higher concern'
    LEVEL_CHOICES = [
        (LEVEL_LOW, LEVEL_LOW),
        (LEVEL_MODERATE, LEVEL_MODERATE),
        (LEVEL_HIGHER, LEVEL_HIGHER),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assessment_results',
    )
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_CHOICES)
    q1_score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)]
    )
    q2_score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)]
    )
    q3_score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)]
    )
    q4_score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)]
    )
    total_score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(12)]
    )
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} {self.assessment_type} ({self.total_score})"
