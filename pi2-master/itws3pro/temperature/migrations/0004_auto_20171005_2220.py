# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0003_temperature_hum_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='lev_value',
            field=models.CharField(default=45, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temperature',
            name='moist_value',
            field=models.CharField(default=23, max_length=250),
            preserve_default=False,
        ),
    ]
