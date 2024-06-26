# Generated by Django 4.2 on 2023-04-17 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_remove_moderator_is_moderator_article_is_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='mainapp.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='mainapp.comment', verbose_name='Родитель'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to='mainapp.author', verbose_name='Автор'),
        ),
    ]
