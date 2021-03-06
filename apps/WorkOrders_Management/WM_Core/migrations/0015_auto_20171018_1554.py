# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-18 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WM_Core', '0014_auto_20171018_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_detail', models.CharField(default='', max_length=15)),
                ('type', models.CharField(default='', max_length=15)),
                ('title', models.CharField(default='', max_length=15)),
                ('comment', models.CharField(default='', max_length=15)),
                ('files', models.CharField(default='', max_length=15)),
                ('date', models.CharField(default='', max_length=15)),
                ('forwarder', models.CharField(default='', max_length=15)),
                ('ticket', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Detail', to='WM_Core.Ticket')),
            ],
            options={
                'verbose_name': 'Detail',
                'verbose_name_plural': 'Details',
            },
        ),
        migrations.RemoveField(
            model_name='note',
            name='ticket',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
