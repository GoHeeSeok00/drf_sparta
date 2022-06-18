from django.db import models

from config.models import BaseModel
from user.models import User as UserModel


# Create your models here.
class Event(models.Model):
    title = models.CharField("제목", max_length=100)
    thumbnail = models.ImageField("썸네일", upload_to="static/event/thumbnail/")
    information = models.TextField("이벤트 정보")
    created_at = models.DateTimeField("등록일", auto_now_add=True)
    start_point = models.DateTimeField("노출 시작 일")
    end_point = models.DateTimeField("노출 종료 일")
    is_activate = models.BooleanField("활성화 여부", default=True)

    def __str__(self):
        return f"{self.title} // {self.start_point} ~ {self.end_point}"


class Product(BaseModel):
    user = models.ForeignKey(to=UserModel, verbose_name="작성자", on_delete=models.CASCADE)
    name = models.CharField("상품명", max_length=100)
    thumbnail = models.ImageField("썸네일", upload_to="static/product/thumbnail/")
    information = models.TextField("상품 정보")
    end_point = models.DateTimeField("노출 종료 일")
    price = models.IntegerField("가격")
    is_activate = models.BooleanField("활성화 여부", default=True)

    def __str__(self):
        return f"{self.name} / {self.price}"


class ProductReview(BaseModel):
    user = models.ForeignKey(to=UserModel, verbose_name="작성자", on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, verbose_name="상품", on_delete=models.CASCADE)
    content = models.TextField("내용")
    rating = models.SmallIntegerField("평점", max_length=3) # 0~5 / 0.5단위

    def __str__(self):
        return f"{self.product} 상품에 대한 {self.user.username}님의 리뷰입니다."

