from rest_framework import serializers

from .models import Setting, Lore


class LoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lore
        fields = ("id", "setting", "content", "created_at", "author")


class SettingSerializer(serializers.ModelSerializer):
    lores = LoreSerializer(many=True, read_only=True)

    class Meta:
        model = Setting
        fields = ("id", "title", "author", "created_at", "lores")

