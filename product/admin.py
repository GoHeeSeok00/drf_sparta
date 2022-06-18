from django.contrib import admin

from product.models import Event as EventModel
from product.models import Product as ProductModel
from product.models import ProductReview as ProductReviewModel

# Register your models here.
admin.site.register(EventModel)
admin.site.register(ProductModel)
admin.site.register(ProductReviewModel)