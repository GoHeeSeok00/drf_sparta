from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from user.models import DevLanguage as DevLanguageModel
from user.models import UserProfileDevLanguage as UserProfileDevLanguage

# Unregister(Group)
admin.site.unregister(Group)

# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)
admin.site.register(DevLanguageModel)
admin.site.register(UserProfileDevLanguage)