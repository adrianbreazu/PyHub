# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambient_data', '0002_auto_20160101_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='read_datetime',
            field=models.DateTimeField(),
        ),
    ]
