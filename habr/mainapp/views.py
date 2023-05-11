from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.schemas import coreapi
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework import generics, status
from .serializers import ArticleSerializer, CommentListSerializer, ArticlesDetailSerializer, CategorySerializer, CommentSerializer, LikeSerializer, AuthorSerializer, ModeratorSerializer, ArticlesListSerializer
from .models import Article, Category, Author, Comment, Like, Moderator

class ArticlesList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesListSerializer

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(is_approved=True, is_published=True).order_by('-updated_at').exclude(is_deleted=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ArticlesListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ArticlesDetailSerializer(instance)
        return Response(serializer.data)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ModeratorViewSet(ModelViewSet):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.data['password']))

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.data['password']))


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentListSerializer(queryset, many=True)
        return Response(serializer.data)

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        from_user=request.data['from_user']

        if request.data['to_user']:
            to_user=request.data['to_user']
            likes= Like.objects.filter(from_user=from_user, to_user=to_user)
        elif request.data['to_comment']:
            to_comment = request.data['to_comment']
            likes=Like.objects.filter(from_user=from_user, to_comment=to_comment)
        elif request.data['to_article']:
            to_article = request.data['to_article']
            likes=Like.objects.filter(from_user=from_user,to_article=to_article)
        else:
            return Response('Лайк должен быть кому-то адресован', status=status.HTTP_400_BAD_REQUEST)
        if likes:
            return Response('Вы уже поставили лайк', status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MyToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'id':user.id})


obtain_auth_token = MyToken.as_view()