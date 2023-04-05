from django.db import models

class User(models.Model):
    username=models.CharField(max_length=64, unique=True, null=False)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    is_moderator = models.BooleanField(default=False)

    def __str__(self):
        return self.username