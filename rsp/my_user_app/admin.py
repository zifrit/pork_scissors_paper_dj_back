from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from . import models


@admin.register(models.CustomUser)
class AdminCustomUser(UserAdmin):
    list_display = ['id',
                    'tg_id',
                    'username',
                    'first_name',
                    'last_name',
                    'is_active',
                    'is_staff']
    list_display_links = ['id', 'username']
    list_editable = ['is_active',
                     'is_staff']
    ordering = ['id', 'username']
    readonly_fields = ['date_update']
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'delete', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined', 'date_update', 'date_delete')
        }),
    )
