from django.contrib import admin
from django.contrib.auth.models import Group

from members.models import User as UserModel
from members.models import UserProfile as UserProfileModel
from members.models import Hobby as HobbyModel
from members.models import DevLanguage as DevLanguageModel
from members.models import UserProfileDevLanguage as UserProfileDevLanguage

# Unregister(Group)
admin.site.unregister(Group)

# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)
admin.site.register(DevLanguageModel)
admin.site.register(UserProfileDevLanguage)