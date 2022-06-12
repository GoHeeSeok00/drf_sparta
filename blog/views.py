from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from user.models import User as UserModel


class _():
    pass


# Create your views here.

class ArticleApiView(APIView):

    def get(self):
        return

    def post(self):
        return

    def put(self):
        return

    def delete(self):
        return
