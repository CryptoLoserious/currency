# Generated by Django 4.2.7 on 2023-12-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0011_alter_contactus_options_remove_contactus_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=128, verbose_name='Path')),
                ('request_method', models.CharField(max_length=8, verbose_name='Request')),
                ('time', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Buy')),
            ],
        ),
    ]
