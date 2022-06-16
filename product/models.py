from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField("제목", max_length=100)
    thumbnail = models.ImageField("썸네일", upload_to="static/thumbnail/")
    information = models.TextField("정보")
    created_at = models.DateTimeField("등록일", auto_now_add=True)
    start_point = models.DateTimeField("노출 시작 일")
    end_point = models.DateTimeField("노출 종료 일")
    is_activated = models.BooleanField("활성화 여부", default=True)

    def __str__(self):
        return f"{self.title} // {self.start_point} ~ {self.end_point}"