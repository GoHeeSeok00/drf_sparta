from atexit import register
from django.contrib import admin

from members.models import User as UserModel
from members.models import UserProfile as UserProfileModel
from members.models import Hobby as HobbyModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)