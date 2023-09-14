import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # user model
    settings = models.ManyToManyField('Setting', through='UserRole', related_name='setings')

class Setting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, through='UserRole', related_name='users')

    def __str__(self):
        return self.title


class Lore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE, related_name="lores")
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.content

class Role(models.TextChoices):
    DM = 'DM', 'Dungeon Master'
    PLAYER = 'PLAYER', 'Player'

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    setting = models.ForeignKey('Setting', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role.choices)


    