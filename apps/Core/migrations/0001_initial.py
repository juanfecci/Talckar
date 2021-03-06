# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 15:57
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models

from django.contrib.contenttypes.models import ContentType

from Core.models import Client as CoreClient
import django.utils.timezone



def create_groups(apps, schema_editor):
    content_type = ContentType.objects.get_for_model(CoreClient)
    permission1 = django.contrib.auth.models.Permission.objects.create(
                                            codename='can_edit',
                                            name='Can Edit',
                                            content_type=content_type,
                                        )
    permission1.save()
    permission2 = django.contrib.auth.models.Permission.objects.create(
                                            codename='can_view',
                                            name='Can View',
                                            content_type=content_type,
                                        )
    permission2.save()


    group, created = django.contrib.auth.models.Group.objects.get_or_create(name='Auditor')
    if created:
        group.permissions.add(permission1)
    group.save()

    group, created = django.contrib.auth.models.Group.objects.get_or_create(name='Client')
    if created:
        group.permissions.add(permission2)
    group.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.RunPython(create_groups),

        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('modules', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Auditor',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
                'permissions': (('can_view_dashboard', 'can_view_dashboard'), ('can_edit_vm', 'can_edit_vm')),
            },
            bases=('Core.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client_User',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
                'permissions': (('can_view_dashboard', 'can_view_dashboard'),),
            },
            bases=('Core.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
