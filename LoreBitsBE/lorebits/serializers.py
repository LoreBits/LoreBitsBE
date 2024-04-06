from rest_framework import serializers

from .models import Setting, Lore, User


class LoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lore
        fields = ("id", "setting", "content", "created_at")


class SettingSerializer(serializers.ModelSerializer):
    lores = LoreSerializer(many=True, read_only=True)

    class Meta:
        model = Setting
        fields = ("id", "title", "created_at", "lores")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)