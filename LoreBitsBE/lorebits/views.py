from rest_framework.generics import  ListCreateAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView

from .models import Setting, Lore
from .serializers import SettingSerializer, LoreSerializer


class SettingListCreate(ListCreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer


class SettingRetrieve(RetrieveAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer


class SettingDestroy(DestroyAPIView):
    queryset = Setting.objects.all()


class LoreCreate(CreateAPIView):
    model = Lore
    serializer_class = LoreSerializer


class LoreDestroy(DestroyAPIView):
    queryset = Lore.objects.all()
