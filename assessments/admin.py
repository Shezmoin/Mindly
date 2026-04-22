from django.contrib import admin

from .models import AssessmentResult


@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'assessment_type', 'total_score', 'level', 'created_at')
    list_filter = ('assessment_type', 'level', 'created_at')
    search_fields = ('user__username', 'user__email')
