from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin
from .serializers import ArticleSerializer, CategorySerializer, CommentSerializer, LikeSerializer, AuthorSerializer, ModeratorSerializer
from .models import Article, Category, Author, Comment, Like, Moderator

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ModeratorViewSet(ModelViewSet):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
