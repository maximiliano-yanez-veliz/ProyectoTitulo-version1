# Generated by Django 4.1 on 2022-09-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanillaEjercicios', '0005_habilidadejercicio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ejercicios',
            options={'ordering': ['titulo', 'subtitulo', 'descripcion'], 'verbose_name': 'Mi Empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.AddField(
            model_name='ejercicios',
            name='habilidades',
            field=models.ManyToManyField(blank=True, through='PlanillaEjercicios.HabilidadEjercicio', to='PlanillaEjercicios.habilidades'),
        ),
    ]