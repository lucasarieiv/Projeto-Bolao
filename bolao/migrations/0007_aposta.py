# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolao', '0006_remove_selecao_pontuacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='aposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_vencedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_vencedor', to='bolao.selecao')),
            ],
        ),
    ]
