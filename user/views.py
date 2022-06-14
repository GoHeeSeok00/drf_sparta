from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from user.models import User as UserModel
from user.models import Hobby as HobbyModel
from user.models import UserProfile as UserProfileModel
from user.models import UserProfileDevLanguage as UserProfileDevLanguageModel
from user.serializers import UserSerializer


class _(): # TODO 자동 임포트시 해당 클래스 위에 생성 // 나중에 삭제
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
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)

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

class UsersApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_serializer = UserSerializer(UserModel.objects.all(), many=True).data
        return Response(user_serializer, status=status.HTTP_200_OK)