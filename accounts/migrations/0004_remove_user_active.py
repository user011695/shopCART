# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-15 05:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180115_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
    ]
