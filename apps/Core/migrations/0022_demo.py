# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0021_user_viajes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_plaza', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Demo',
                'verbose_name_plural': 'Demos',
            },
        ),
    ]
