# Generated by Django 5.0.2 on 2024-09-23 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia_telefonica_ejercito', '0002_alter_contacto_correo_inst_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
