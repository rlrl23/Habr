from django.db import models
from users.models import User

# class User(models.Model):
#     username=models.CharField(max_length=64, unique=True, null=False)
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     email = models.EmailField(unique=True)
#     is_moderator = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.username


class Category(models.TextChoices):
    disign='Дизайн'
    web='Web разработка'
    mobile='Мобильная разработка'
    marleting='Маркетинг'


class Article(models.Model):
    category=models.CharField(verbose_name='Категория', max_length=20, choices=Category.choices, default=Category.web, null=False)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    short_description = models.TextField(max_length=300, verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(User, verbose_name='Автор статьи', on_delete=models.PROTECT,
                               related_name='article_author')
    created_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, db_index=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    is_deleted = models.BooleanField(verbose_name='Удалена', default=True)

    def __str__(self):
        return self.title


class Comment:
    pass


class Like:
    pass
