# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dns', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Asset',
                'verbose_name_plural': 'Assets',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('port', models.CharField(max_length=50, null=True)),
                ('statusCode', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('asset', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='VIM_Core.Asset')),
            ],
            options={
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
        ),
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateTimeField(default='', max_length=15)),
                ('finishDate', models.DateTimeField(default='', max_length=15)),
                ('status', models.CharField(choices=[('WT', 'En espera'), ('PA', 'Pausado'), ('RU', 'Corriendo'), ('RU', 'Terminado')], default='', max_length=300)),
                ('percent', models.CharField(max_length=50, null=True)),
                ('assets', models.ManyToManyField(to='VIM_Core.Asset')),
            ],
            options={
                'verbose_name': 'Scan',
                'verbose_name_plural': 'Scans',
            },
        ),
        migrations.AddField(
            model_name='picture',
            name='scan',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='VIM_Core.Scan'),
        ),
    ]
