from django.urls import path
from product.views import EventApiView

app_name = "product"

urlpatterns = [
    path('', EventApiView.as_view(), name='event'),  # class엔 as_view()를 붙여주어야 한다.
]