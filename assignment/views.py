from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from user.models import User as UserModel

# Create your views here.

class Assignment(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        data = {
            "message": "Success!!!"
        }
        # ★★ 역참조 Test ★★
        user = UserModel.objects.get(id=1)  # result: 오브젝트
        # print(dir(user))
        dev_languages = user.userprofile.userprofiledevlanguage_set.all()  # result: 쿼리셋 // 정참조 + 역참조
        # print(dev_languages)
        for language in dev_languages:  # language = object
            # print(dir(language.userprofile))
            language_member = language.dev_language.userprofiledevlanguage_set.all().exclude(
                userprofile=user.userprofile).annotate(
                userprofile__user__fullname=F('userprofile__user__fullname')).values_list("userprofile__user__fullname",
                                                                                          flat=True)  # 가독성 제로 코드,,
            language_member = list(language_member)
            print(f"개발언어: {language.dev_language} / 멤버 : {language_member}")

        hobbys = user.userprofile.hobby.all()  # result: 쿼리셋 // 정참조
        # print(hobbys)
        # print(type(hobbys))
        for hobby in hobbys:
            hobby_members = hobby.userprofile_set.exclude(user=user).annotate(fullname=F("user__fullname")).values_list(
                "fullname", flat=True)  # 역참조
            hobby_members = list(hobby_members)
            print(f"취미: {hobby} / 멤버: {hobby_members}")
        return Response(data)
