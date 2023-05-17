from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
# from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        # superuser = User.objects.create_superuser(
        #     username='admin',
        #     email='admin@test.ru',
        #     password='paraNoiya245'
        # )
        User.objects.create_user(
            username='user1',
            email='user1@test.ru',
            password='paraNoiya24'
        )
        User.objects.create_user(
            username='user2',
            email='user2@test.ru',
            password='paraNoiya24'
        )
        User.objects.create_user(
            username='user3',
            email='user3@test.ru',
            password='paraNoiya24'
        )
