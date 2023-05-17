from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug.fields import AutoSlugField


class User(AbstractUser):
    #password=models.CharField(max_length=14)
    is_moderator = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "Все пользователи"
        verbose_name_plural="Все пользователи"

class Moderator(User):

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "Модератор"
        verbose_name_plural = "Модераторы"

class Author(User):
    date_of_birth = models.DateField(null=True, blank=True)
    description = models.TextField()
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Category(models.Model):
    name=models.CharField(verbose_name='Категория', max_length=30)
    slug=AutoSlugField(populate_from='name', editable=True, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Категория', related_name='category_name')
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    short_description = models.TextField(max_length=300, verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(Author, verbose_name='Автор статьи', on_delete=models.PROTECT,
                               related_name='article_author')
    created_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, db_index=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    is_deleted = models.BooleanField(verbose_name='Удалена', default=True)
    is_approved=models.BooleanField(verbose_name='Проверена модератором', default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text=models.TextField(null=False, verbose_name='text')
    user=models.ForeignKey(Author, on_delete=models.CASCADE, null=False, related_name='comment_author',
                    verbose_name='Автор')
    article= models.ForeignKey(Article, on_delete=models.CASCADE, null=True, related_name='comment_article',
                    verbose_name='Статья')
    parent_id= models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='parent',
                    verbose_name='Родитель')
    created_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, db_index=True)

    def __str__(self):
        return self.text

class Like(models.Model):
    from_user=models.ForeignKey(Author, on_delete=models.CASCADE, null=False, related_name='like_from')
    to_user=models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='like_to')
    to_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, related_name='liked_comment')
    to_article=models.ForeignKey(Article, on_delete=models.CASCADE, null=True, related_name='liked_article')
    datetime=models.DateTimeField(auto_now_add=True)

