from django.db import models


# basemodel / 작성시간, 수정시간
class BaseModel(models.Model):
    created_at = models.DateTimeField("작성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정 시간", auto_now=True)

    class Meta:
        abstract = True