from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from articles.serializers import ArticleSerializer
from articles.models import Article

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
