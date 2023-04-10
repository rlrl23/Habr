from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin
from articles.serializers import ArticleSerializer
from articles.models import Article, Category

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# class CategoryViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
