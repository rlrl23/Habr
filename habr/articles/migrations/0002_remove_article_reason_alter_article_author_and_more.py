# Generated by Django 4.2 on 2023-04-05 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='reason',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_author', to='users.user', verbose_name='Автор статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Дизайн', 'Disign'), ('Web разработка', 'Web'), ('Мобильная разработка', 'Mobile'), ('Маркетинг', 'Marleting')], default='Web разработка', max_length=20, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=True, verbose_name='Удалена'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
