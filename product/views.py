import datetime

from django.utils import timezone
from rest_framework import permissions, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Event as EventModel
from product.models import Product as ProductModel
from product.serializers import EventSerializer, ProductSerializer

""""""
# custom permission
class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class IsAdminIsAuthenticatedThreeDaysFromJoinDateIsNotAuthenticatedReadOnly(permissions.BasePermission):
    """
    admin 사용자는 모두 가능
    로그인 후 3일 경과 모두 가능
    로그인 안한 경우 조회만 가능
    """
    SAFE_METHODS = ('GET', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user
        method = request.method

        if not user.is_authenticated and method in self.SAFE_METHODS:
            return True
        elif not user.is_authenticated:
            response = {
                "detail": "서비스를 이용하기 위해 로그인 해주세요.",
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)
        elif user.is_admin:
            return True
        elif user.is_authenticated and bool(user.join_date + datetime.timedelta(days=3) < timezone.now()):
            return True
        elif user.is_authenticated and method in self.SAFE_METHODS:
            return True
        return False

# Create your views here.
class EventApiView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        # 이벤트 시작 <= now < 종료
        event_serializer = EventSerializer(EventModel.objects.filter(
            start_point__lte=timezone.now(),
            end_point__gt=timezone.now(),
            is_activate=True
        ), many=True)
        return Response(event_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # request 데이터로 Event serializer 생성
        event_serializer = EventSerializer(data=request.data)

        # request print
        # print(request.data)
        # print(type(request.data))

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



class ProductApiView(APIView):
    permission_classes = [IsAdminIsAuthenticatedThreeDaysFromJoinDateIsNotAuthenticatedReadOnly]

    def get(self, request):
        product_serializer = ProductSerializer(ProductModel.objects.filter(
            end_point__gt=timezone.now(),
            is_activate=True
        ), many=True)
        if request.user.is_authenticated:
            my_product_serializer = ProductSerializer(ProductModel.objects.filter(
                user=request.user
            ), many=True)
            return Response({
                "products": product_serializer.data,
                "my_products": my_product_serializer.data}, status=status.HTTP_200_OK)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data["user"] = request.user.id
        product_serializer = ProductSerializer(data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response({"message": "상품 등록이 완료되었습니다."}, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            # 업데이트할 object 가져오기
            data = request.data
            product = ProductModel.objects.get(id=data["obj_id"])
            product_serializer = ProductSerializer(product, data=data, partial=True)
            product_serializer.is_valid(raise_exception=True)
            product_serializer.save()
            return Response({"message": "상품 수정이 완료되었습니다."}, status=status.HTTP_200_OK)

        except EventModel.DoesNotExist:
            return Response({"error": "상품을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        return