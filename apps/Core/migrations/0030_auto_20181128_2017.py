# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0029_auto_20181128_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='viajes',
            field=models.ManyToManyField(related_name='user', to='Core.Viaje'),
        ),
    ]
