from django.urls import path

from .views import SettingRandomLore ,RandomLore, SettingListCreate, SettingRetrieve, LoreCreate, LoreDestroy, SettingDestroy

urlpatterns = [
    path("settings/", SettingListCreate.as_view(), name="setting-list"),
    path("settings/<str:pk>", SettingRetrieve.as_view(), name="setting-retrieve"),
    path("settings/<str:pk>/destroy", SettingDestroy.as_view(), name="setting-destroy"),
    path("lores/", LoreCreate.as_view(), name="lore-create"),
    path("lores/<str:pk>/destroy", LoreDestroy.as_view(), name="lore-destroy"),
    path("settings/random", RandomLore.as_view(), name="random-lore"),
    path("settings/<str:pk>/random", SettingRandomLore.as_view(), name="setting-random-lore")
    ]
