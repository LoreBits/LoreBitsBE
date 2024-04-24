from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Setting, Lore, User, UserRole, Role
from .serializers import SettingSerializer, LoreSerializer, UserSerializer


class SettingListCreate(ListCreateAPIView):
    serializer_class = SettingSerializer

    def get_queryset(self):
        if self.request.user.pk:
            return Setting.objects.filter(users=self.request.user.pk)
        else:
            return Setting.objects.none()

    def perform_create(self, serializer):
        setting = serializer.save(author=self.request.user)
        UserRole.objects.create(user=self.request.user, setting=setting, role=Role.DM)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class SettingDetailView(RetrieveAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    lookup_field = 'pk'  #  TODO: Change to SETTING_CODE when we get to it (or something else idk, wyjebane)


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


class CreateUserView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
