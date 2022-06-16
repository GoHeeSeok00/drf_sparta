from django.utils import timezone
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Event as EventModel
from product.serializers import EventSerializer



""""""
# Create your views here.
class EventApiView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        # 이벤트 시작 <= now < 종료
        event_serializer = EventSerializer(EventModel.objects.filter(
            start_point__lte=timezone.now(),
            end_point__gt=timezone.now(),
            is_activated=True
        ), many=True)
        return Response(event_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # request 데이터로 Event serializer 생성
        event_serializer = EventSerializer(data=request.data)
        print(request.data)
        print(type(request.data))
        # 유효성 검사, 실패 시 message 띄움
        event_serializer.is_valid(raise_exception=True)
        # 데이터 저장
        event_serializer.save()
        return Response({"message": "이벤트 등록이 완료되었습니다."}, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            # 업데이트할 object 가져오기
            data = request.data
            event = EventModel.objects.get(id=data["obj_id"])
            event_serializer = EventSerializer(event, data=data, partial=True)
            event_serializer.is_valid(raise_exception=True)
            event_serializer.save()
            return Response({"message": "이벤트 수정이 완료되었습니다."}, status=status.HTTP_200_OK)

        except EventModel.DoesNotExist:
            return Response({"error": "이벤트를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
