# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIM_Core', '0006_picture_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='idTask',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='finishDate',
            field=models.DateTimeField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='startDate',
            field=models.DateTimeField(blank=True, max_length=15, null=True),
        ),
    ]
