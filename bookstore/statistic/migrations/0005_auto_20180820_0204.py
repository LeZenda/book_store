# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-20 02:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0004_auto_20180820_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestsat',
            name='get',
        ),
        migrations.RemoveField(
            model_name='requestsat',
            name='post',
        ),
        migrations.RemoveField(
            model_name='requestsat',
            name='raw_post',
        ),
    ]