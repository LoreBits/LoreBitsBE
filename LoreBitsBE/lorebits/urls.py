from django.urls import path

from .views import SettingListCreate, SettingRetrieve, LoreCreate, LoreDestroy, SettingDestroy, CreateUserView

urlpatterns = [
    path("settings/", SettingListCreate.as_view(), name="setting-list"),
    path("settings/<str:pk>", SettingRetrieve.as_view(), name="setting-retrieve"),
    path("settings/<str:pk>/destroy", SettingDestroy.as_view(), name="setting-destroy"),
    path("lores/", LoreCreate.as_view(), name="lore-create"),
    path("lores/<str:pk>/destroy", LoreDestroy.as_view(), name="lore-destroy"),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    ]
