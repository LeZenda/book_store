# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-19 13:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestSat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('host', models.CharField(max_length=1000)),
                ('path', models.CharField(max_length=1000)),
                ('method', models.CharField(max_length=50)),
                ('uri', models.CharField(max_length=2000)),
                ('status_code', models.IntegerField()),
                ('user_agent', models.CharField(blank=True, max_length=1000, null=True)),
                ('remote_addr', models.GenericIPAddressField()),
                ('remote_addr_fwd', models.GenericIPAddressField(blank=True, null=True)),
                ('meta', models.TextField()),
                ('cookies', models.TextField(blank=True, null=True)),
                ('get', models.TextField(blank=True, null=True)),
                ('post', models.TextField(blank=True, null=True)),
                ('raw_post', models.TextField(blank=True, null=True)),
                ('is_secure', models.BooleanField()),
                ('is_ajax', models.BooleanField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]