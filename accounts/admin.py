from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gt_email', 'phone_number', 'created_at']
    search_fields = ['user__username', 'gt_email']
    readonly_fields = ['created_at']
