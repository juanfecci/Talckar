# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HearthBeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('UP', 'Arriba'), ('DOWN', 'Abajo')], max_length=3)),
                ('date', models.DateField(auto_now_add=True)),
                ('responseTime', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'HearthBeat',
                'verbose_name_plural': 'HearthBeats',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('url', models.CharField(max_length=15)),
                ('statusCode', models.CharField(choices=[('404', '404 - Not found'), ('200', '200 - OK'), ('302', '302 - Redirect')], max_length=3)),
                ('textResponse', models.TextField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
            },
        ),
        migrations.AddField(
            model_name='hearthbeat',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Site', to='HS_Core.Site'),
        ),
    ]
