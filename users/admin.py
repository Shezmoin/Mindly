<<<<<<< HEAD
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, UserProfile


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription_tier', 'joined_date', 'reminder_time')
    list_filter = ('subscription_tier', 'joined_date')
    search_fields = ('user__username', 'user__email')
=======
# Register your models here.
>>>>>>> 04c11c74a48edb4abaea6dc8325a8cb21860f238
