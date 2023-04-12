from rest_framework.serializers import ModelSerializer
from .models import Article, Category, Author, Comment, Like, Moderator

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        prepopulated_fields={'slug':('name',)}

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['username','first_name','last_name','email','password','date_of_birth','description', 'is_banned']

class ModeratorSerializer(ModelSerializer):
    class Meta:
        model = Moderator
        fields = ['username','first_name','last_name','email','password']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'