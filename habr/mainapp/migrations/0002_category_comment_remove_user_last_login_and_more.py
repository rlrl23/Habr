# Generated by Django 4.2 on 2023-04-10 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Категория')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('parent_id', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата обновления')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_author', to='mainapp.user', verbose_name='Автор статьи'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='mainapp.user')),
                ('to_article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.article')),
                ('to_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.comment')),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_author', to='mainapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.article'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория'),
        ),
    ]