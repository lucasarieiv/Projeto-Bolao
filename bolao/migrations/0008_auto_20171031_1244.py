# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolao', '0007_aposta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aposta',
            name='time_vencedor',
        ),
        migrations.AddField(
            model_name='aposta',
            name='aposta_partida',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='aposta_partida', to='bolao.Partida'),
            preserve_default=False,
        ),
    ]
