# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 05:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bolao', '0021_aposta_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aposta',
            name='usuario',
        ),
    ]
