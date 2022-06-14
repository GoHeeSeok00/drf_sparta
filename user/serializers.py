from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from user.models import UserProfileDevLanguage as UserProfileDevLanguageModel
from user.models import DevLanguage as DevLanguageModel

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        # serializer에 사용될 model, field지정
        model = HobbyModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["name"]


class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)
    class Meta:
        # serializer에 사용될 model, field지정
        model = UserProfileModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["introduction", "age", "birthday", "hobby"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    class Meta:
        # serializer에 사용될 model, field지정
        model = UserModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["username", "fullname", "password", "email", "join_date", "userprofile"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
