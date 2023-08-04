import random 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

class SettingRandomLore(APIView):
    def get(self, request):
        setting_ids = Setting.objects.values_list('id', flat=True)  # Pobieramy listę wszystkich ID obiektów Setting
        if setting_ids:
            random_setting_id = random.choice(setting_ids)  # Losowo wybieramy ID ustawienia
            lore_objects = Lore.objects.filter(setting=random_setting_id)  # Pobieramy obiekty Lore powiązane z ustawieniem
            if lore_objects:
                random_lore = random.choice(lore_objects)  # Losowo wybieramy obiekt Lore związany z wylosowanym ustawieniem
                serializer = LoreSerializer(random_lore)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "No data available."}, status=status.HTTP_404_NOT_FOUND)
