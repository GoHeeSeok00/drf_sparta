from datetime import datetime

from django.db.models import Count, Avg
from django.utils import timezone
from rest_framework import serializers


from product.models import Event as EventModel
from product.models import Product as ProductModel
from product.models import ProductReview as ProductReviewModel


""""""
# Event serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = ["title", "thumbnail", "information", "start_point", "end_point"]



class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReviewModel
        fields = ["user", "product", "content", "rating", "created_at"]
        read_only_fields = ["user", "product"] # 사용자와 상품은 읽기 전용 / created_at 필드는 자동으로 읽기전용(auto_now_add)



class ProductSerializer(serializers.ModelSerializer):
    # 리뷰를 가져올 필드를 만들어줌
    reviews = serializers.SerializerMethodField()
    reviews_data = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ["user", "name", "thumbnail", "information", "price", "end_point",
                  "created_at", "reviews", "reviews_data"]

    # 리뷰 가져올 함수
    def get_reviews(self, obj_id):
        # 최신 리뷰 가져오기
        product_review_query = ProductReviewModel.objects.order_by("-id").filter(product_id=obj_id).first()
        review_serializer = ProductReviewSerializer(product_review_query)
        return review_serializer.data

    def get_reviews_data(self, odj_id):
        product_query = ProductModel.objects.filter(id=odj_id.id).annotate(
            review_counts = Count('productreview'),
            review_average = Avg('productreview__rating')
        )
        return {"count": product_query[0].review_counts, "average": round(product_query[0].review_average, 2)}



    # validate 함수 선언 시 serializer에서 자동으로 해당 함수의 validation을 해줌
    def validate(self, data):
        print(data)
        # custom validation pattern
        if data.get("end_point", "") < timezone.now():
            # validation에 통과하지 못할 경우 ValidationError class 호출
            raise serializers.ValidationError(
                # custom validation error message
                detail={"error": "노출이 종료된 상품을 등록할 수 없습니다."},
            )

        # validation에 문제가 없을 경우 data return
        return data

    def create(self, validated_data):
        validated_data["information"] += f"\r\n{timezone.now().strftime('%Y-%m-%d')}에 등록된 상품입니다."
        instance = ProductModel.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        # instance에는 입력된 object가 담긴다.

        try: # validated_data에 information 정보가 있으면 실행
            validated_data["information"] = f"{timezone.now().strftime('%Y-%m-%d')}에 수정되었습니다. " \
                                            f"\r\n{validated_data['information']}"
        except KeyError: # information 없으면 keyerror 발생 // instance에서 데이터 가져와서 넣어주기
            validated_data["information"] = f"{timezone.now().strftime('%Y-%m-%d')}에 수정되었습니다. " \
                                            f"\r\n{instance.information}"

        for key, value in validated_data.items():
            # update 에서는 일부 필드만 수정할 수도 있기 때문에 setattr 사용
            setattr(instance, key, value)
        instance.save()
        return instance