from django.urls import path
from product.views import EventApiView, ProductApiView

app_name = "product"

urlpatterns = [
    path('', ProductApiView.as_view(), name='product'), # class엔 as_view()를 붙여주어야 한다.
    path('event/', EventApiView.as_view(), name='event'),
    # path('product/review/', ProductApiView.as_view(), name='product_review'),
]