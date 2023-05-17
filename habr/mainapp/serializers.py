import datetime
from rest_framework.serializers import ModelSerializer, DateTimeField, ReadOnlyField, RelatedField, \
    PrimaryKeyRelatedField, SerializerMethodField, StringRelatedField
from .models import Article, Category, Author, Comment, Like, Moderator


class ArticleSerializer(ModelSerializer):
    created_at = DateTimeField(format='%d.%m.%Y', default=datetime.datetime.now())
    updated_at = DateTimeField(format='%d.%m.%Y', default=datetime.datetime.now())

    class Meta:
        model = Article
        fields = ['id', 'category', 'author', 'created_at', "updated_at", "title", "short_description",
                  "full_description", "is_published", "is_deleted", 'is_approved']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        prepopulated_fields = {'slug': ('name',)}


class ModeratorSerializer(ModelSerializer):
    class Meta:
        model = Moderator
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'is_moderator']


class CommentListSerializer(ModelSerializer):
    created_at = DateTimeField(format='%H-%M  %d.%m.%Y', default=datetime.datetime.now())
    updated_at = DateTimeField(format='%H-%M  %d.%m.%Y', default=datetime.datetime.now())
    user = StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    created_at = DateTimeField(format='%H-%M  %d.%m.%Y', default=datetime.datetime.now())
    updated_at = DateTimeField(format='%H-%M  %d.%m.%Y', default=datetime.datetime.now())

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(ModelSerializer):
    datetime = DateTimeField(format='%H-%M  %d.%m.%Y', default=datetime.datetime.now())

    class Meta:
        model = Like
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    is_moderator = ReadOnlyField()

    # from_user=LikeSerializer(read_only=True)
    # to_user=LikeSerializer(read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'date_of_birth', 'description',
                  'is_banned', 'is_moderator']


class ArticlesListSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = StringRelatedField(read_only=True)
    liked_article = SerializerMethodField()
    comment_article = SerializerMethodField()
    created_at = DateTimeField(format='%d.%m.%Y', default=datetime.datetime.now())
    updated_at = DateTimeField(format='%d.%m.%Y', default=datetime.datetime.now())

    def get_comment_article(self, instance):
        return instance.comment_article.count()

    def get_liked_article(self, instance):
        return instance.liked_article.count()

    class Meta:
        model = Article
        fields = ['id', 'category', 'author', 'created_at', "updated_at", "title", "short_description",
                  "full_description", "is_published", "is_deleted", 'is_approved', 'comment_article', 'liked_article']


class ArticlesDetailSerializer(ModelSerializer):
    category = StringRelatedField(read_only=True)
    author = StringRelatedField(read_only=True)
    author_id = ReadOnlyField()
    liked_article = SerializerMethodField()
    comment_article = SerializerMethodField()
    created_at = DateTimeField(format='%d.%m.%Y', default=datetime.datetime.now())
    updated_at = DateTimeField(format='%d.%m.%Y', default=datetime.datetime.now())

    def get_comment_article(self, instance):
        return instance.comment_article.count()

    def get_liked_article(self, instance):
        return instance.liked_article.count()

    class Meta:
        model = Article
        fields = ['id', 'category', 'author', 'author_id', 'created_at', "updated_at", "title", "short_description",
                  "full_description", "is_published", "is_deleted", 'is_approved', 'comment_article', 'liked_article']


class ArticlesCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'author', 'category', 'short_description', 'full_description', 'is_published')
