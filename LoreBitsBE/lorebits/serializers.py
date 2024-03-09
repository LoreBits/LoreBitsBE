from rest_framework import serializers

from .models import Setting, Lore, User


class LoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lore
        fields = ("id", "setting", "content", "created_at", "author")


class SettingSerializer(serializers.ModelSerializer):
    lores = LoreSerializer(many=True, read_only=True)

    class Meta:
        model = Setting
        fields = ("id", "title", "author", "created_at", "lores")


class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']  #'snippets']