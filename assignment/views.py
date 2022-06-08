from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework import permissions

# Create your views here.

class Assignment(APIView):
    # permission_classes = permissions.AllowAny
    def get(self, request):
        return HttpResponse({"message": "Success!!!"})
