from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.schemas import coreapi
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework import generics
from .serializers import ArticleSerializer, CommentListSerializer, ArticlesDetailSerializer, CategorySerializer, \
    CommentSerializer, LikeSerializer, AuthorSerializer, ModeratorSerializer, ArticlesListSerializer, \
    ArticlesCreateSerializer
from .models import Article, Category, Author, Comment, Like, Moderator


class ArticlesList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesListSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ArticlesCreateSerializer
        return ArticlesDetailSerializer


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


class MyToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'id': user.id})


obtain_auth_token = MyToken.as_view()
