# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolao', '0017_aposta_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aposta',
            name='aposta_partida',
            field=models.CharField(max_length=100),
        ),
    ]
