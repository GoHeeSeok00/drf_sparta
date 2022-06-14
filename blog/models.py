from django.db import models

from config.models import BaseModel
from user.models import User as UserModel


class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=50)
    information = models.TextField("카테고리 정보")

    def __str__(self):
        return self.name


# 게시글 모델 / article model
class Article(BaseModel):
    user = models.ForeignKey(to=UserModel, verbose_name="사용자", on_delete=models.CASCADE)
    category = models.ManyToManyField(to=Category, verbose_name="카테고리")
    title = models.CharField("제목", max_length=100)
    content = models.TextField("내용")


    def __str__(self):
        return f"{self.user}의 게시글: {self.title}"


# 댓글 모델 / comment model
class Comment(BaseModel):
    article = models.ForeignKey(to=Article, verbose_name="게시글", on_delete=models.CASCADE)
    user = models.ForeignKey(to=UserModel, verbose_name="사용자", on_delete=models.CASCADE)
    comment = models.CharField("댓글", max_length=200)

    def __str__(self):
        return f"게시글: {self.article} / 댓글 작성자: {self.user}"
