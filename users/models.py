from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(blank=True, null=True)


class UserProfile(models.Model):
    TIER_FREE = 'free'
    TIER_PREMIUM = 'premium'
    SUBSCRIPTION_CHOICES = [
        (TIER_FREE, 'Free'),
        (TIER_PREMIUM, 'Premium'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    subscription_tier = models.CharField(max_length=10, choices=SUBSCRIPTION_CHOICES, default=TIER_FREE)
    joined_date = models.DateField(auto_now_add=True)
    reminder_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} profile"


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
