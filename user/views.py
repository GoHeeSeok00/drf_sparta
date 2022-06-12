from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.db.models import F

from user.models import User as UserModel
from user.models import Hobby as HobbyModel
from user.models import UserProfile as UserProfileModel
from user.models import UserProfileDevLanguage as UserProfileDevLanguageModel

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

    # use custom permission
    # permission_classes = [UserLevelPermission]

    def get(self, request):
        # users = UserModel.objects.all()
        users = UserModel.objects.all().values_list("fullname", flat=True) # values_list 실험 코드
        users = list(users)

        return Response(users)

    def post(self, request):
        return Response()

    def put(self, request):
        return Response()

    def delete(self, request):
        return Response()


class UserProfileApiView(APIView):
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]

    # use custom permission
    # permission_classes = [UserLevelPermission]

    def get(self, request):
        userprofile = UserProfileModel.objects.filter()
        return Response(userprofile)

    def post(self, request):
        return Response()

    def put(self, request):
        return Response()

    def delete(self, request):
        return Response()

