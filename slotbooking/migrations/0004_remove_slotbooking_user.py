# Generated by Django 2.2 on 2021-10-22 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slotbooking', '0003_slotbooking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slotbooking',
            name='user',
        ),
    ]