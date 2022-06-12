from django.db import models

# Create your models here.
from user.models import User as UserModel


class Category(models.Model):
    tag = models.CharField("카테고리 이름", max_length=50)
    information = models.TextField("카테고리 정보")

    def __str__(self):
        return self.tag


class Article(models.Model):
    user = models.ForeignKey(to=UserModel, verbose_name="사용자", on_delete=models.CASCADE)
    category = models.ManyToManyField(to=Category, verbose_name="카테고리")
    title = models.CharField("제목", max_length=100)
    content = models.TextField("내용")
    created_at = models.DateTimeField("작성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정 시간", auto_now=True)

    def __str__(self):
        return f"{self.user}의 게시글: {self.title}"