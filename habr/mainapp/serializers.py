import datetime
from rest_framework.serializers import ModelSerializer, DateTimeField, ReadOnlyField
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
        prepopulated_fields={'slug':('name',)}

class AuthorSerializer(ModelSerializer):
    is_moderator=ReadOnlyField()
    class Meta:
        model = Author
        fields = ['id','username','first_name','last_name','email','password','date_of_birth','description', 'is_banned', 'is_moderator']

class ModeratorSerializer(ModelSerializer):
    class Meta:
        model = Moderator
        # fields = ['id','username','first_name','last_name','email','password', 'is_moderator']
        # fields = ['id','username','first_name','last_name','email','password']
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