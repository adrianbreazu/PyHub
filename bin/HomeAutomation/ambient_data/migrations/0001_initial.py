# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CommunicationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='ReadData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=70)),
                ('value', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ReadDataRecurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recurrency', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_number', models.UUIDField()),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('read_datetime', models.DateTimeField(auto_now=True)),
                ('board_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambient_data.BoardType')),
                ('communication_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambient_data.CommunicationType')),
                ('read_data_recurrency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambient_data.ReadDataRecurrency')),
            ],
        ),
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='sensor_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambient_data.SensorType'),
        ),
        migrations.AddField(
            model_name='readdata',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambient_data.Sensor'),
        ),
    ]
