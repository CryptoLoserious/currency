# Generated by Django 5.0.1 on 2024-01-20 18:49

import currency.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('email_from', models.EmailField(max_length=128, verbose_name='Email from')),
                ('subject', models.CharField(max_length=256, verbose_name='Subject')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('body', models.CharField(max_length=2048, verbose_name='Body')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=128, verbose_name='Path')),
                ('request_method', models.CharField(max_length=8, verbose_name='Request')),
                ('time', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Buy')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=255, verbose_name='URL')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('logo', models.FileField(blank=True, default=None, null=True, upload_to=currency.models.logo_directory_path, verbose_name='Logo')),
                ('code_name', models.CharField(max_length=64, unique=True, verbose_name='Code name')),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Buy')),
                ('sell', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Sell')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('currency_type', models.IntegerField(choices=[(1, 'Dollar'), (2, 'Euro'), (3, 'Bitcoin'), (4, 'Ethereum')], default=1, verbose_name='Currency type')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency.source')),
            ],
        ),
    ]
