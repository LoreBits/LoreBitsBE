from django.urls import path

from .views import SettingListCreate, LoreCreate, LoreDestroy, SettingDestroy, CreateUserView, SettingDetailView

urlpatterns = [
    path('settings/<str:pk>/', SettingDetailView.as_view(), name='setting-detail'),
    path("settings/<str:pk>/destroy", SettingDestroy.as_view(), name="setting-destroy"),
    path("settings/", SettingListCreate.as_view(), name="setting-list"),
    path("lores/", LoreCreate.as_view(), name="lore-create"),
    path("lores/<str:pk>/destroy", LoreDestroy.as_view(), name="lore-destroy"),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
]
