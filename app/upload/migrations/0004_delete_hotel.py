# Generated by Django 4.2.3 on 2024-01-28 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_rename_shop_hotel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]