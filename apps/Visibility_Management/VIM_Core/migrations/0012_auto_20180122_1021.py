# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIM_Core', '0011_scan_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='idTask',
            field=models.CharField(default='A', max_length=50, null=True),
        ),
    ]
