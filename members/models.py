
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=20)
    fullname = models.CharField("이름", max_length=20)
    join_date = models.DateTimeField("가입일", auto_now_add=True)

    level = models.IntegerField("사용자 권한", default=1) # 1: 뉴비 ··· 9: 관리자

class UserProfile(models.Model):
    user = models.OneToOneField(to=User, verbose_name="사용자", on_delete=models.CASCADE, primary_key=True)
    hobby = models.ManyToManyField(to="Hobby", verbose_name="취미")
    introduction = models.TextField("소개", default="안녕하세요")
    age = models.IntegerField("나이")
    birthday = models.DateField("생일")

class Hobby(models.Model):
    hobby = models.CharField("취미", max_length=20)