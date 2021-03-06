# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-15 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WM_Core', '0003_auto_20170913_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=15)),
                ('user', models.CharField(max_length=15)),
                ('method', models.CharField(max_length=15)),
                ('event', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=15)),
                ('ticket', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='WM_Core.Ticket')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
        migrations.AlterModelOptions(
            name='inbox',
            options={'verbose_name': 'Inbox', 'verbose_name_plural': 'Inboxs'},
        ),
    ]
