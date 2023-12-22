# Generated by Django 4.2.7 on 2023-12-01 20:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_remove_rate_source_source_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='source',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rate',
            name='currency_type',
            field=models.IntegerField(choices=[(1, 'Dollar'), (2, 'Euro'), (3, 'Bitcoin'), (4, 'Ethereum')], default=1),
        ),
    ]