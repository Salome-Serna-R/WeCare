# Generated by Django 5.1 on 2024-11-05 03:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0005_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]