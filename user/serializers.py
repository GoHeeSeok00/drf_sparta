from rest_framework import serializers

from blog.models import Article as ArticleModel
from blog.models import Category as CategoryModel
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from user.models import UserProfileDevLanguage as UserProfileDevLanguageModel
from user.models import DevLanguage as DevLanguageModel



class _: # TODO 나중에 삭제
    pass


# DevLanguage serializer
class DevLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevLanguageModel
        fields = ["name"]


# 개발언어 관계테이블 serializer
class UserProfileDevLanguageSerializer(serializers.ModelSerializer):
    dev_language = DevLanguageSerializer()
    class Meta:
        model = UserProfileDevLanguageModel
        fields = ["dev_language"]


# DevLanguage serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["name"]


# article serializer
class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = ArticleModel
        fields = ["title", "category"]


# hobby serializer
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = HobbyModel
        fields = ["name"]


# userprofile serializer
class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)
    userprofiledevlanguage_set = UserProfileDevLanguageSerializer(many=True)
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "age", "birthday", "hobby", "userprofiledevlanguage_set"]


# user serializer
class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article_set = ArticleSerializer(many=True)
    class Meta:
        # serializer에 사용될 model, field지정
        model = UserModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["username", "fullname", "password", "email", "join_date", "userprofile", "article_set"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
