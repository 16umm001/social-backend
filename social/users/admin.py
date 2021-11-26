from django.contrib import admin

from social.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # fields = [
    #     'id',
    #     'username',
    #     'email',
    #     'password1',
    #     'password2',
    #     'first_name',
    #     'last_name',
    #     'phone_number',
    #     'is_active',
    #     'is_staff',
    #     'is_superuser',
    #     'modified_at',
    #     'last_login'
    # ]

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
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name"
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "modified_at",
                )
            }
        )
    )

    list_display = [
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'phone_number',
        'is_active',
        'is_staff',
        'is_superuser',
        'modified_at',
        'last_login'
    ]

    readonly_fields = ['id', 'modified_at']

    def save_model(self, request, obj, form, change):

        super(UserAdmin, self).save_model(request, obj, form, change)
