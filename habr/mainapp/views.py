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
    # print('User:queryset:', queryset)

    # def list(self, request, *args, **kwargs):
    #     queryset = User.objects.all()
    #     # serializer_class = UserForAllSerializer
    #     serializer = UserForAllSerializer(queryset, many=True)
    #     context = {'request': request}
    #     return Response(serializer.data)
    #     # pass

    def get_serializer_class(self):
        # print('\nUserViewSet:self.request.user', self.request.user)
        # print('\nUserViewSet:self.request.data', self.request.data)
        # print('\nUserViewSet:self.request.auth', self.request.auth)
        # print('\nUserViewSet:self.request.dir', self.request.__dir__())
        # print('\nUserViewSet:self.request.dict', self.request.__dict__)
        # print('\nUserViewSet:self.request.parser_context',
        #       self.request.parser_context)
        # print('\nUserViewSet:self.request.parser_context.keys()',
        #       self.request.parser_context.keys())
        # print('\nUserViewSet:self.request.parser_context.get(\'kwargs\').get(\'pk\')',
        #       self.request.parser_context.get('kwargs').get('pk'))
        # print('\nUserViewSet:self.request.path', self.request.path)
        # print('\nUserViewSet:self.request.path_info', self.request.path_info)
        user_pk = self.request.parser_context.get('kwargs').get('pk')
        # print('\nUserViewSet::user_pk', user_pk)
        # print('\nself.queryset.get(pk=user_pk)', self.queryset.get(pk=user_pk))
        # print('*' * 15)
        if self.request.user.is_staff:
            # print('\nSTAFF!!!\n')
            return UserForAdminSerializer
        if self.request.user.is_authenticated and \
                user_pk is not None and \
                self.request.user == self.queryset.get(pk=user_pk):
                # self.request.user == self.queryset.get(username=self.request.user):
            # print('\n\nOWNER!!!\n')
            # print('\nself.queryset.get(pk=user_pk)', self.queryset.get(pk=user_pk))
            return UserForOwnerSerializer
        return UserForAllSerializer


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     # x = User.objects.get(pk=self.request.user)
#
#     def get_serializer_class(self):
#         if self.request.user.is_authenticated and \
#                 self.request.user == self.queryset.get(username=self.request.user):
#             print('self.request.user:', self.request.user)
#             return UserForOwnerSerializer
#         # if self.request.user.is_authenticated:
#         #     print('self.request.user:', self.request.user)
#         #     if self.request.user == self.queryset.get(username=self.request.user):
#         #         print('self.request.user:', self.request.user)
#         #         return UserForOwnerSerializer
#         return UserForAllSerializer
#     # if IsAdminUser.has_permission():
#     #     serializer_class = UserForAdminSerializer
#     # else:
#     #     serializer_class = UserForAllSerializer
#     # queryset = User.objects.all()
#     # serializer_class = UserSerializer
#
#     # def list(self, request, *args, **kwargs):
#     #     queryset = User.objects.all()
#     #     serializer = UserSerializer
#     #     return Response(serializer.data)


class ArticleViewSet(ModelViewSet):
    # permission_classes = [IsAuthor]
    # permission_classes = (IsAuthorExists,)
    queryset = Article.objects.all()
    # print('view.ArticleViewSet:queryset:', queryset)
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

    # def get_serializer_class(self):
    #     pass

# class ArtList(ListModelMixin):
#     pass

# class MclassRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     pass


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    # print('view.Category:queryset:', queryset)
    serializer_class = CategorySerializer


class ModeratorViewSet(ModelViewSet):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer


class AuthorViewSet(ModelViewSet):
    permission_classes = (IsAdminOrModerator,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # def get_permissions(self):
    #     permission_classes = (IsAdminOrModerator,)
    #     if self.action in ('create', 'destroy'):
    #         permission_classes = (IsAdminUser,)
    #     else:
    #         permission_classes = (IsAuthenticatedOrReadOnly,)
    #     return [permission() for permission in permission_classes]

    # def retrieve(self, request, *args, **kwargs):
    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        # author = get_object_or_404(self.queryset, pk=pk)
        author = get_object_or_404(queryset, pk=pk)
        # serializer = AuthorSerializer(author)
        serializer = AuthorDetailSerializer(author)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
