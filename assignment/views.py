from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

# Create your views here.

class Assignment(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        data = {
            "message": "Success!!!"
        }
        return Response(data)
