from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.schemas import coreapi
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import ArticleSerializer, CommentListSerializer, ArticlesDetailSerializer, CategorySerializer, \
    CommentSerializer, LikeSerializer, AuthorSerializer, ModeratorSerializer, ArticlesListSerializer, \
    ArticlesCreateSerializer, ProfileSerializer
from .models import Article, Category, Author, Comment, Like, Moderator


class ArticlesList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesListSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ArticlesCreateSerializer
        return ArticleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

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


class AuthorViewSet(ModelViewSet, APIView):
    permission_classes = [permissions.AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.data['password']))


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


class Profile(APIView):
    def get(self, request, *args, **kwargs):
        user_id = Token.objects.filter(key=request.headers['Authorization'].replace('Token ', '')).first().user_id
        author = Author.objects.filter(user_ptr_id=user_id).first()
        return Response(ProfileSerializer(author).data)

    def post(self, request, *args, **kwargs):
        user_id = Token.objects.filter(key=request.headers['Authorization'].replace('Token ', '')).first().user_id
        author = Author.objects.filter(user_ptr_id=user_id).first()
        data = request.data
        author.username = data['username']
        author.first_name = data['first_name']
        author.last_name = data['last_name']
        author.description = data['description']
        author.date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
        author.save()
        return Response(ProfileSerializer(author).data)


obtain_auth_token = MyToken.as_view()
