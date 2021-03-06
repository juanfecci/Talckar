# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WM_Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='following',
            options={'verbose_name': 'Following', 'verbose_name_plural': 'Followings'},
        ),
        migrations.AddField(
            model_name='following',
            name='active',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='following',
            name='last_escaling',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='following',
            name='service',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='following',
            name='ticket',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='WM_Core.Ticket'),
        ),
        migrations.AddField(
            model_name='inbox',
            name='active',
            field=models.CharField(default=True, max_length=15),
        ),
        migrations.AddField(
            model_name='inbox',
            name='date',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='inbox',
            name='forwarder',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='inbox',
            name='ticket',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='WM_Core.Ticket'),
        ),
        migrations.AddField(
            model_name='note',
            name='ticket',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='WM_Core.Ticket'),
        ),
    ]
