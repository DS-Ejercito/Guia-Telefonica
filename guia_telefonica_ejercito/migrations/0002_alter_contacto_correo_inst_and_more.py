# Generated by Django 5.0.2 on 2024-09-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia_telefonica_ejercito', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='correo_inst',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='correo_personal',
            field=models.CharField(max_length=100),
        ),
    ]
