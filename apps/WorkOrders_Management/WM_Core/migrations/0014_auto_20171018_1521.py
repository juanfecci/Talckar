# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-18 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WM_Core', '0013_auto_20170925_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='id_note',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='note',
            name='comment',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='note',
            name='files',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='note',
            name='forwarder',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='note',
            name='type',
            field=models.CharField(default='', max_length=15),
        ),
    ]
