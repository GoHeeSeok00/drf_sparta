from django.urls import path
from members.views import UserApiView

app_name = "members"

urlpatterns = [
    path('', UserApiView.as_view(), name='user'),  # class엔 as_view()를 붙여주어야 한다.
]