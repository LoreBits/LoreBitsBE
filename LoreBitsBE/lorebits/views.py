from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Setting, Lore, User, UserRole, Role
from .serializers import SettingSerializer, LoreSerializer


class SettingListCreate(ListCreateAPIView):
    serializer_class = SettingSerializer

    def get_queryset(self):
        return Setting.objects.filter(users=self.request.user.pk)

    def perform_create(self, serializer):
        setting = serializer.save(author=self.request.user)
        UserRole.objects.create(user=self.request.user, setting=setting, role=Role.DM)


    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class SettingRetrieve(RetrieveAPIView):
    serializer_class = SettingSerializer

    def get_queryset(self):
        return Setting.objects.filter(users=self.request.user.pk)


class SettingDestroy(DestroyAPIView):
    queryset = Setting.objects.all()

    def get_queryset(self):
        return Setting.objects.filter(author=self.request.user)


class LoreCreate(CreateAPIView):
    model = Lore
    serializer_class = LoreSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LoreDestroy(DestroyAPIView):

    def get_queryset(self):
        return Lore.objects.filter(author=self.request.user)
