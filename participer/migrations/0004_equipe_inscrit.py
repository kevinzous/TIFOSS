# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-09 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participer', '0003_auto_20170928_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='inscrit',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
