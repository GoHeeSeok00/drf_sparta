from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from user.models import User as UserModel
from user.models import Hobby as HobbyModel
from user.models import UserProfile as UserProfileModel
from user.models import UserProfileDevLanguage as UserProfileDevLanguageModel


class _():
    pass


# Custom permissions
class UserLevelPermission(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.level > 8)

        return result


# Create your views here.
class UserApiView(APIView):
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]

    # custom permission
    # permission_classes = [UserLevelPermission]

    def get(self, request):
        if request.user.is_authenticated: # 로그인이 되어있다면
            # objects.get에서 객체가 존재하지 않을 경우 DoesNotExist Exception 발생
            try:
                user = UserModel.objects.get(id=request.user.id)
                user_profile = user.userprofile
                profile_data = {
                    "이름": user.fullname,
                    "나이": user_profile.age,
                    "생일": user_profile.birthday,
                    # "취미": list(user_profile.hobby.all()),
                    # "개발언어": list(user_profile.userprofiledevlanguage_set.all()),
                    "소개": user_profile.introduction,
                }

                user_articles = user.article_set.all()
                articles_data = []
                for user_article in user_articles:
                    articles_data.append(user_article.title)

                data = {
                    "프로필": profile_data,
                    "게시글": articles_data,
                }

                return Response(data)

            except UserModel.DoesNotExist:
                # some event
                return Response("존재하지 않는 사용자입니다.", status=status.HTTP_404_NOT_FOUND)
        else: # 로그인 X
            return Response("로그인이 필요합니다.")


    def post(self, request):
        return Response()


    def put(self, request):
        return Response()

    def delete(self, request):
        return Response()


# 로그인 view
class LoginApiView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self):
        return
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


# 로그아웃 view
class LogoutApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self):
        return

    def post(self, request):
        logout(request)
        return Response({"message": "로그아웃 성공!!"}, status=status.HTTP_200_OK)


class UserProfileApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        userprofile = UserProfileModel.objects.filter()
        return Response(userprofile)

    def post(self, request):
        return Response()

    def put(self, request):
        return Response()

    def delete(self, request):
        return Response()

