# Generated by Django 5.0.7 on 2024-09-08 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0002_rename_descripcion_comentario_texto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='imagen',
        ),
    ]
