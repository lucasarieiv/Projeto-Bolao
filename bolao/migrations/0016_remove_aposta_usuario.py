# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bolao', '0015_aposta_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aposta',
            name='usuario',
        ),
    ]
