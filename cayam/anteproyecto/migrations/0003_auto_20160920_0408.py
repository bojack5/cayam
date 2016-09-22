# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-20 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anteproyecto', '0002_auto_20160919_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='total',
        ),
        migrations.AlterField(
            model_name='anteproyecto',
            name='descripcion',
            field=models.TextField(error_messages={'required': 'Porfavor llena este campo!'}),
        ),
        migrations.AlterField(
            model_name='anteproyecto',
            name='impacto_del_proyecto',
            field=models.CharField(error_messages={'required': 'Porfavor llena este campo!'}, max_length=140),
        ),
        migrations.AlterField(
            model_name='anteproyecto',
            name='nombre',
            field=models.CharField(error_messages={'required': 'Porfavor llena este campo!'}, max_length=140),
        ),
        migrations.AlterField(
            model_name='anteproyecto',
            name='principal',
            field=models.ManyToManyField(error_messages={'required': 'Porfavor llena este campo!'}, related_name='PartidaP', to='anteproyecto.Partida'),
        ),
        migrations.AlterField(
            model_name='anteproyecto',
            name='secundario',
            field=models.ManyToManyField(error_messages={'required': 'Porfavor llena este campo!'}, related_name='PartidaS', to='anteproyecto.Partida'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='cantidad',
            field=models.IntegerField(default=1, error_messages={'required': 'Porfavor llena este campo!'}),
        ),
        migrations.AlterField(
            model_name='partida',
            name='descripcion',
            field=models.CharField(error_messages={'required': 'Porfavor llena este campo!'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='partida',
            name='importe',
            field=models.FloatField(error_messages={'required': 'Porfavor llena este campo!'}),
        ),
    ]