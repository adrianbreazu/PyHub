# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 19:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ambient_data', '0003_auto_20160101_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='readdata',
            name='read_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 1, 19, 56, 40, 80698, tzinfo=utc)),
            preserve_default=False,
        ),
    ]