# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-11 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='paye',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joueur',
            name='paye',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
