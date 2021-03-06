# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-20 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WM_Core', '0008_auto_20170920_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='inbox_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='client',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='group_asigned',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='id_petition',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='id_workOrder',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='notes',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='resume',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status_cause',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status_note',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user_asigned',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
