# Generated by Django 4.1 on 2022-09-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanillaEjercicios', '0002_alter_ejercicios_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejercicios',
            name='subtitulo',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
    ]
