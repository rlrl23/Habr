from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, \
    get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin
from .serializers import ArticleSerializer, CategorySerializer, \
    CommentSerializer, LikeSerializer, AuthorSerializer, ModeratorSerializer, \
    UserForAdminSerializer, UserForAllSerializer, UserForOwnerSerializer, \
    AuthorDetailSerializer
from .models import Article, Category, Author, Comment, Like, Moderator
from .habr_permissions import IsAuthor, IsAuthorExists, IsAdminOrModerator


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        user_pk = self.request.parser_context.get('kwargs').get('pk')
        if self.request.user.is_staff:
            return UserForAdminSerializer
        if self.request.user.is_authenticated and \
                user_pk is not None and \
                self.request.user == self.queryset.get(pk=user_pk):
            return UserForOwnerSerializer
        return UserForAllSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = (IsAuthorExists,)
        elif self.action in ('update', 'partial_update'):
            permission_classes = (IsAuthor,)
        elif self.action == 'destroy':
            permission_classes = (IsAdminUser, IsAuthor)
        else:
            permission_classes = (IsAuthenticatedOrReadOnly,)
        return [permission() for permission in permission_classes]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ModeratorViewSet(ModelViewSet):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer


class AuthorViewSet(ModelViewSet):
    permission_classes = (IsAdminOrModerator,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorDetailSerializer(author)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
