# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolao', '0011_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='aposta',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete='usuario', to='bolao.UserProfile', to_field='id'),
            preserve_default=False,
        ),
    ]
