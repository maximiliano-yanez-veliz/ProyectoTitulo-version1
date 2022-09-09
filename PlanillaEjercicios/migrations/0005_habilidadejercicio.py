# Generated by Django 4.1 on 2022-09-09 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlanillaEjercicios', '0004_habilidades_alter_ejercicios_subtitulo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HabilidadEjercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='descripcion')),
                ('ejercicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PlanillaEjercicios.ejercicios')),
                ('habilidades', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PlanillaEjercicios.habilidades')),
            ],
        ),
    ]