from django.contrib import admin
from .models import Category, Article, Comment, Like
# from .models import CustomUser, Category, Article, Comment, Like

# admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
