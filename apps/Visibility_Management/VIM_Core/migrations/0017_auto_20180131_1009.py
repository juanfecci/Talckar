# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-31 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VIM_Core', '0016_auto_20180131_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='proxy',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='scan',
            name='proxyFtp',
            field=models.CharField(blank=True, default='0', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='proxyFtpPort',
            field=models.CharField(blank=True, default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='proxyHttp',
            field=models.CharField(blank=True, default='0', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='proxyHttpPort',
            field=models.CharField(blank=True, default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='proxySocks',
            field=models.CharField(blank=True, default='0', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='proxySocksPort',
            field=models.CharField(blank=True, default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='proxySsl',
            field=models.CharField(blank=True, default='0', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='proxySslPort',
            field=models.CharField(blank=True, default='0', max_length=10, null=True),
        ),
    ]
