from django.contrib import admin

from blog.models import Category as CategoryModel
from blog.models import Article as ArticleModel

# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(ArticleModel)