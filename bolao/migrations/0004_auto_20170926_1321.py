# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolao', '0003_auto_20170919_1424'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Aposta',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='estadio',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='gol1',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='gol2',
        ),
        migrations.AddField(
            model_name='partida',
            name='local',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='partida',
            name='placar_time1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='placar_time2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
