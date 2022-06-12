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

        # ★★ 역참조 Test ★★
        user = UserModel.objects.get(id=1) # result: 오브젝트
        # print(dir(user))
        dev_languages = user.userprofile.userprofiledevlanguage_set.all() # result: 쿼리셋 // 정참조 + 역참조
        # print(dev_languages)
        for language in dev_languages: # language = object
            # print(dir(language.userprofile))
            language_member = language.dev_language.userprofiledevlanguage_set.all().exclude(userprofile=user.userprofile).annotate(userprofile__user__fullname=F('userprofile__user__fullname')).values_list("userprofile__user__fullname", flat=True) # 가독성 제로 코드,,
            language_member = list(language_member)
            print(f"개발언어: {language.dev_language} / 멤버 : {language_member}")


        hobbys = user.userprofile.hobby.all() # result: 쿼리셋 // 정참조
        # print(hobbys)
        # print(type(hobbys))
        for hobby in hobbys:
            hobby_members = hobby.userprofile_set.exclude(user=user).annotate(fullname=F("user__fullname")).values_list("fullname", flat=True) # 역참조
            hobby_members = list(hobby_members)
            print(f"취미: {hobby} / 멤버: {hobby_members}")

        
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

