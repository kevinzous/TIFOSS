# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-28 12:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participer', '0002_auto_20170811_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forfait',
            old_name='repasDimanche',
            new_name='repas',
        ),
        migrations.RemoveField(
            model_name='forfait',
            name='repasSamedi',
        ),
    ]
