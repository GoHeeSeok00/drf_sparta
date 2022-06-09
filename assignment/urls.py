from django.urls import path
from assignment.views import Assignment

app_name = "assignment"

urlpatterns = [
    path('', Assignment.as_view(), name='assignment'),  # class엔 as_view()를 붙여주어야 한다.
]