from django.urls import path
from blog.views import ArticleApiView

app_name = "blog"

urlpatterns = [
    path('', ArticleApiView.as_view(), name='article'),  # class엔 as_view()를 붙여주어야 한다.
]