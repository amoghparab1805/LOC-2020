from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm
from .models import *


# Our custom user model.
class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class UserAdmin(UserAdmin):
    form = UserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "phone_number",
                )
            },
        ),
    )

admin.site.register(User, UserAdmin)

# Remove groups from admin site.
admin.site.unregister(Group)
