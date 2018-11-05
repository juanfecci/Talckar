# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-29 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ASE_Core', '0006_auto_20180129_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='asset',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='ip',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='asset',
        ),
        migrations.AddField(
            model_name='tag',
            name='assets',
            field=models.ManyToManyField(blank=True, to='ASE_Core.Asset'),
        ),
    ]
