# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-27 02:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0044_user_valoraciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='valoraciones',
        ),
    ]