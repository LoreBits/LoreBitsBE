from django.contrib import admin

from .models import Setting, Lore, User, UserRole

admin.site.register(Setting)

admin.site.register(Lore)

admin.site.register(User)

admin.site.register(UserRole)

# Register your models here.
