# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-02-06 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyapp', '0011_auto_20200205_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='materialno',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
