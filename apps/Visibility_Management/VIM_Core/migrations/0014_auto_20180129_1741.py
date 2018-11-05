# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-29 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ASE_Core', '0007_auto_20180129_1741'),
        ('VIM_Core', '0013_auto_20180129_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finding',
            name='url',
        ),
        migrations.AddField(
            model_name='finding',
            name='asset',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='finding', to='ASE_Core.Asset'),
        ),
    ]
