# Generated by Django 2.2 on 2021-10-22 11:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('slotbooking', '0007_auto_20211022_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slotbooking',
            name='user',
        ),
        migrations.AddField(
            model_name='slotbooking',
            name='user',
            field=models.ManyToManyField(blank=True, max_length=100, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]