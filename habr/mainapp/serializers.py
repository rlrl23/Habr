import datetime

from django.contrib.auth.models import User
from rest_framework import request
from rest_framework.fields import HiddenField
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
        # fields = '__all__'
        # fields = ['id', 'url', 'username', 'first_name', 'last_name',
        #           'email', 'is_staff', 'is_active', 'date_joined']
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

    # is_moderator = ReadOnlyField()
    # author = UserForAllSerializer()

    # def create(self, validated_data):
    #     print('AuthorSerializer:validated_data:', validated_data)
    #     author_ = validated_data.get('author')
    #     print(author_)
    #     users_ = User.objects.all()
    #     print('users_')
    #     print([i for i in users_])
    #     return

    # def delete(self):
    #     pass

    class Meta:
        model = Author
        # fields = '__all__'
        # fields = ['url', 'author']
        fields = ['author']
        # fields = ['id', 'username', 'first_name', 'last_name',
        #           'email', 'password', 'date_of_birth', 'description',
        #           'is_banned', 'is_moderator']


# class AuthorDetailSerializer(HyperlinkedModelSerializer):
class AuthorDetailSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class CurrentAuthorDefault1:
    # requires_context = True
    # def __init__(self):
    #     self.user_id = None

    # def __init__(self):
    #     self.author = None

    def set_context(self, serializer_field):
        user_id = serializer_field.context['request'].user.id
        print('Author.objects.get(author=user_id)',
              Author.objects.get(author=user_id))
        self.author = Author.objects.get(author=user_id)

    # def __call__(self, serializer_field):
    #     return serializer_field.context['request'].user
    #
    # def __repr__(self):
    #     return '%s()' % self.__class__.__name__
    # pass
    def __call__(self):
        print('serializer: self.author:', self.author)
        print('serializer: type(self.author):', type(self.author))
        return self.author

    def __repr__(self):
        return '%s()' % self.__class__.__name__
        # return unicode_to_repr('%s()' % self.__class__.__name__)


# class SomeSerializer(serializers.ModelSerializer):
#     type = serializers.SerializerMethodField()
#
#     def get_type(self, obj):
#         return self.context['view'].kwargs['type'].upper()

# class AuthorSerializer(ModelSerializer):
# class ArticleSerializer(ModelSerializer):

class CurrentAuthorDefault(CurrentUserDefault):
    def __call__(self, serializer_field):
        return int(serializer_field.context['request'].user.id)


# class CurrentUserDefault:
#     requires_context = True
#
#     def __call__(self, serializer_field):
#         return int(serializer_field.context['request'].user.id)
#
#     def __repr__(self):
#         return '%s()' % self.__class__.__name__


class ArticleSerializer(HyperlinkedModelSerializer):
    def create(self, validated_data):
        validated_data['author'] = Author.objects.get(
            author=self.context["request"].user
        )
        # print("validated_data[author]", validated_data['author'])
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


# class ArticleSerializer(HyperlinkedModelSerializer):
#     def get_special_field(self, obj):
#         pass
#
#     def get_current_author(self):
#         return self.context['request'].user
#         # pass
#
#     # category = CategorySerializer(read_only=True)
#     # -----------------------
#     # xxx = FromContext()
#     # xxx = get_serializer_context()
#     # -----------------------
#     # myyyy = get_current_author()
#     # print('serializer: myyyy', myyyy)
#     # print('self.context[\'request\'].user', self.context['request'].user)
#     x = CurrentUserDefault()
#     print('*' * 45, '\nCurrentUserDefault', x)
#     print(type(x))
#     # print('x.__dir__()', x.__dir__())
#     # print('x.__dict__', x.__dict__)
#     print('x.__str__', x.__str__())
#     # print('x.__repr__', x.__repr__())
#     # author = AuthorSerializer(default=CurrentUserDefault(),
#     #                           read_only=True)
#     x = CurrentAuthorDefault1()
#     print('*' * 45, '\nCurrentAuthorDefault', x)
#     print(type(x))
#     # print('x.__dir__()', x.__dir__())
#     # print('x.__dict__', x.__dict__)
#     print('x.__str__', x.__str__())
#     # print('x.__repr__', x.__repr__())
#
#     aaa = Author.objects.get(pk=1).author
#     print('serializer: Author.author', aaa)
#     # Author.get(pk=)
#
#     # user = self.context['request'].user
#     user = CurrentAuthorDefault()
#     print("serializer: user", user)
#     print("serializer: type(user)", type(user))
#     # print("serializer: int(user)", int(user))
#     # Author.objects.get(author=user)
#     print("serializer: Author.objects.get(author=user)",
#           Author.objects.get(author=user.id))
#
#     # author = HiddenField(default=CurrentUserDefault(),)
#     author = HiddenField(default=Author.objects.get(pk=1),)
#     # author = HiddenField(default=CurrentAuthorDefault(),)
#     # author_id = HiddenField(default=CurrentAuthorDefault(),)
#     # author = AuthorSerializer(default=CurrentAuthorDefault(),)
#     created_at = DateTimeField(format='%d.%m.%Y',
#                                read_only=True,
#                                # default=datetime.datetime.now()
#                                )
#     updated_at = DateTimeField(format='%d.%m.%Y',
#                                read_only=True,
#                                # default=datetime.datetime.now()
#                                )
#
#     class Meta:
#         model = Article
#         fields = ['id', 'url', 'category',
#                   'author',
#                   'author_id',
#                   'created_at',
#                   "updated_at",
#                   "title", "short_description", "full_description",
#                   "is_published", "is_deleted", 'is_approved']
#         read_only_fields = (
#             'author',
#             'created_at',
#             'updated_at')


class ModeratorSerializer(ModelSerializer):
    user_moder = UserForAllSerializer()

    class Meta:
        model = Moderator
        # fields = ['id','username','first_name','last_name','email','password', 'is_moderator']
        # fields = ['id','username','first_name','last_name','email','password']
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
