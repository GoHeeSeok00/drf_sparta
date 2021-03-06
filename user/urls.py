from django.urls import path
from user.views import UserApiView, LoginApiView, LogoutApiView

app_name = "user"

urlpatterns = [
    path('', UserApiView.as_view(), name='user'),  # class엔 as_view()를 붙여주어야 한다.
    path('login/', LoginApiView.as_view(), name='login'),  # class엔 as_view()를 붙여주어야 한다.
    path('logout/', LogoutApiView.as_view(), name='logout'),  # class엔 as_view()를 붙여주어야 한다.
]