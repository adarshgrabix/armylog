# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-01-24 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyapp', '0002_issueregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueregister',
            name='issueqty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='issueregister',
            name='quantityheld',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='issueregister',
            name='subdepot',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantityrecieved',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='subdepot',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='wtratio',
            field=models.IntegerField(),
        ),
    ]
