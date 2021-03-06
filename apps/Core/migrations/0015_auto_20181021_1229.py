# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0014_auto_20181021_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_parada', models.IntegerField(blank=True, null=True)),
                ('coordenada_x', models.IntegerField(blank=True, null=True)),
                ('coordenada_y', models.IntegerField(blank=True, null=True)),
                ('hora', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Parada',
                'verbose_name_plural': 'Paradas',
            },
        ),
        migrations.CreateModel(
            name='Plaza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_plaza', models.IntegerField(blank=True, null=True)),
                ('posicion', models.IntegerField(blank=True, null=True)),
                ('mascota', models.BooleanField(default=True)),
                ('caracteristica', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Plazas',
                'verbose_name_plural': 'Plazas',
            },
        ),
        migrations.CreateModel(
            name='Trayecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_parada', models.IntegerField(blank=True, null=True)),
                ('precio', models.IntegerField(blank=True, null=True)),
                ('destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ParadaDestino', to='Core.Parada')),
                ('origen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ParadaOrigen', to='Core.Parada')),
            ],
            options={
                'verbose_name': 'Trayecto',
                'verbose_name_plural': 'Trayectos',
            },
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_viaje', models.IntegerField(blank=True, null=True)),
                ('maletero', models.BooleanField(default=True)),
                ('mascota', models.BooleanField(default=True)),
                ('tarifaPreferencias', models.IntegerField(blank=True, null=True)),
                ('paradas', models.ManyToManyField(to='Core.Parada')),
                ('trayectos', models.ManyToManyField(to='Core.Trayecto')),
            ],
            options={
                'verbose_name': 'Viaje',
                'verbose_name_plural': 'Viajes',
            },
        ),
        migrations.AlterField(
            model_name='conductor',
            name='foto_vehiculo',
            field=models.ImageField(upload_to='autos'),
        ),
    ]
