# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-19 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anteproyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
