# Generated by Django 4.2.3 on 2023-07-31 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lorebits', '0002_alter_setting_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lore',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lorebits.setting')),
            ],
        ),
    ]