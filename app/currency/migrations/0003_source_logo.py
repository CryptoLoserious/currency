# Generated by Django 4.2.7 on 2023-12-26 19:32

import currency.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_alter_source_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='logo',
            field=models.FileField(blank=True, default=None, null=True, upload_to=currency.models.logo_directory_path, verbose_name='Logo'),
        ),
    ]