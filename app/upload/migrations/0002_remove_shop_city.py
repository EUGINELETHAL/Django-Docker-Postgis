# Generated by Django 4.2.3 on 2024-01-28 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='city',
        ),
    ]