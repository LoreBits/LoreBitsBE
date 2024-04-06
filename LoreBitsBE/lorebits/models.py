import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    def _create(self, email, password=None, is_superuser=False, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_staff = is_superuser
        user.is_active = True
        user.is_superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create(email, password, is_superuser=True, **extra_fields)

    def create_user(self, email, password=None, **extra_fields):
        return self._create(email, password, is_superuser=False, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField('Email address', unique=True)
    settings = models.ManyToManyField('Setting', through='UserRole', related_name='setings')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


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
