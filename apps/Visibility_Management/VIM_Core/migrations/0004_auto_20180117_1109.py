# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIM_Core', '0003_auto_20180117_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='percent',
            field=models.CharField(default='0', max_length=50, null=True),
        ),
    ]
