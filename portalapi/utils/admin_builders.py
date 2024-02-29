from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for the User model.

    This admin class extends the default UserAdmin provided by Django
    and customizes the display and organization of fields in the Django admin.

    Attributes:
        list_display (tuple): Fields displayed in the list view of the admin.
        fieldsets (tuple): Fieldsets to organize fields in the detail view of the admin.

    Note:
        Ensure that the field names in list_display and fieldsets match the actual
        field names in the User model.
    """

    list_display = (
        "username",
        "email",
        "contact",
        "is_contact_verified",
        "is_email_verified",
        "is_staff",
    )

    fieldsets = list(UserAdmin.fieldsets) + [  # type: ignore
        (
            "Profile Fields",
            {
                "fields": (
                    "contact",
                    "role",
                    "is_contact_verified",
                    "is_email_verified",
                ),
            },
        ),
    ]
