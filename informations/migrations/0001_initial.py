# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-12 20:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=80)),
                ('ecole', models.CharField(max_length=50)),
                ('identifiant', models.IntegerField()),
                ('paye', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='forfait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hebergement', models.BooleanField()),
                ('repasSamedi', models.BooleanField()),
                ('repasDimanche', models.BooleanField()),
                ('soiree', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='joueur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('taille', models.CharField(choices=[('S', 'taille S'), ('M', 'taille M'), ('L', 'taille L'), ('XL', 'taille XL')], default='S', max_length=2)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1)),
                ('ecole', models.CharField(max_length=50)),
                ('paye', models.BooleanField()),
                ('forfait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informations.forfait')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informations.equipe')),
            ],
        ),
        migrations.AddField(
            model_name='equipe',
            name='joueurs',
            field=models.ManyToManyField(to='informations.joueur'),
        ),
    ]
