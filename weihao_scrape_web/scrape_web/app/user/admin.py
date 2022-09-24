from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from app.user.models import UserProfile
from utils.admin import admin_site


class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'mobile', 'is_staff', 'date_joined')
    search_fields = ('username', 'mobile', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = UserAdmin.fieldsets + (
        ('基本信息', {'fields': ('mobile',)}),
    )


admin_site.register(UserProfile, UserProfileAdmin)
