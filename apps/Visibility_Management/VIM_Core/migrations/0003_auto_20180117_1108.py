# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIM_Core', '0002_auto_20180117_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='finishDate',
            field=models.DateTimeField(blank=True, default='', max_length=15, null=True),
        ),
    ]