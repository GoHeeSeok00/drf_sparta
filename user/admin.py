from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from user.models import DevLanguage as DevLanguageModel
from user.models import UserProfileDevLanguage as UserProfileDevLanguage


class UserProfileInline(admin.StackedInline):
    model = UserProfileModel
    filter_horizontal = ("hobby", )


class UserAdmin(BaseUserAdmin):
    list_display = ("id", "username", "fullname")
    list_display_links = ("id", "username")
    list_filter = ("username", "fullname")
    search_fields = ("username", "fullname")
    readonly_fields = ("username", "join_date")

    fieldsets = (
        ("info", {"fields": ("username", "password", "email", "fullname", "join_date")}),
        ("permissions", {"fields": ("is_admin", "is_active", "permission_level")})
    )

    inlines = (
        UserProfileInline,
    )

    filter_horizontal = []


# Unregister(Group)
admin.site.unregister(Group)

# Register your models here.
admin.site.register(UserModel, UserAdmin)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)
admin.site.register(DevLanguageModel)
admin.site.register(UserProfileDevLanguage)