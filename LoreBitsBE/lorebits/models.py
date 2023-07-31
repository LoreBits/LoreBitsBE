import uuid
from django.utils import timezone


from django.db import models
from django.contrib.auth.models import User



class Setting(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL ,null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lore(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL ,null=True , blank=True)


# Create your models here.
