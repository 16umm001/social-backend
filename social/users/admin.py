from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from social.users.models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": ('is_active', 'is_verified', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "modified_at",
                )
            }
        )
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide", ),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )

    list_display = [
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_verified',
        'is_active',
        'is_staff',
        'is_superuser',
        'modified_at',
        'last_login'
    ]

    readonly_fields = ['id', 'modified_at', 'last_login']
