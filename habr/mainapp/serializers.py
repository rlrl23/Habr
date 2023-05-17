import datetime

from django.contrib.auth.models import User
# from rest_framework import request
# from rest_framework.fields import HiddenField
from rest_framework.serializers import (
    ModelSerializer, DateTimeField, ReadOnlyField,
    HyperlinkedModelSerializer,
    CurrentUserDefault
)
from .models import Article, Category, Author, Comment, Like, Moderator


# class UserSerializer(ModelSerializer):
class UserForAllSerializer(HyperlinkedModelSerializer):
    print()

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'url', 'username')


class UserForAdminSerializer(HyperlinkedModelSerializer):
    print()

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'url', 'username', 'first_name', 'last_name',
                  'email', 'is_staff', 'is_active', 'date_joined']


class UserForOwnerSerializer(HyperlinkedModelSerializer):
    print()

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'first_name', 'last_name',
                  'email', 'is_active', 'date_joined']


# class CategorySerializer(ModelSerializer):
class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        prepopulated_fields = {'slug': ('name',)}


# class AuthorSerializer(ModelSerializer):
class AuthorSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ['author']


class AuthorDetailSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


# class CurrentAuthorDefault1:
#
#     def set_context(self, serializer_field):
#         user_id = serializer_field.context['request'].user.id
#         print('Author.objects.get(author=user_id)',
#               Author.objects.get(author=user_id))
#         self.author = Author.objects.get(author=user_id)
#
#     def __call__(self):
#         print('serializer: self.author:', self.author)
#         print('serializer: type(self.author):', type(self.author))
#         return self.author
#
#     def __repr__(self):
#         return '%s()' % self.__class__.__name__
#
#
# class CurrentAuthorDefault(CurrentUserDefault):
#     def __call__(self, serializer_field):
#         return int(serializer_field.context['request'].user.id)


class ArticleSerializer(HyperlinkedModelSerializer):
    def create(self, validated_data):
        validated_data['author'] = Author.objects.get(
            author=self.context["request"].user
        )
        return Article.objects.create(**validated_data)

    class Meta:
        model = Article
        fields = ('id', 'url', 'category', 'author',
                  'title', 'short_description', 'full_description',
                  'created_at', 'updated_at',
                  'is_published', 'is_deleted', 'is_approved')
        read_only_fields = (
            'author',
            'created_at',
            'updated_at'
        )


class ModeratorSerializer(ModelSerializer):
    user_moder = UserForAllSerializer()

    class Meta:
        model = Moderator
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    created_at = DateTimeField(format='%H-%M  %d.%m.%Y',
                               default=datetime.datetime.now())
    updated_at = DateTimeField(format='%H-%M  %d.%m.%Y',
                               default=datetime.datetime.now())

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class LikeSerializer(ModelSerializer):
    datetime = DateTimeField(format='%H-%M  %d.%m.%Y',
                             default=datetime.datetime.now())

    class Meta:
        model = Like
        fields = '__all__'
