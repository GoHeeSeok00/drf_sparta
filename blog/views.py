import datetime

from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from blog.models import Category as CategoryModel
from blog.models import Article as ArticleModel


""""""
# custom permission
class ThreeDaysFromJoinDate(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.join_date + datetime.timedelta(days=3) < timezone.now())
        return result


# Create your views here.
class ArticleApiView(APIView):
    # use custom permission: 가입후 3일이 지난 사용자
    permission_classes = [ThreeDaysFromJoinDate]
    def get(self):
        return

    def post(self, request):
        title = request.data.get("title", "")
        content = request.data.get("content", "")
        categorys = request.data.get("categorys", "")
        # print(categorys)
        # print(type(categorys))

        category_querysets = CategoryModel.objects.filter(tag__in=categorys)
        # article instance 생성
        article = ArticleModel.objects.create(user_id=request.user.id, title=title, content=content)
        article.category.set(category_querysets)
        article.save()

        return Response("게시글 작성 성공!!", status=status.HTTP_200_OK)

    def put(self):
        return

    def delete(self):
        return
