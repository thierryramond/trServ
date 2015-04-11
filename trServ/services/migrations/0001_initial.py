# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
                ('service_du', models.IntegerField(default=192)),
                ('decharge', models.IntegerField(default=192)),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nature', models.CharField(max_length=20)),
                ('enseignant', models.ForeignKey(to='services.Enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='Ue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('titre', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20)),
                ('année', models.CharField(max_length=20)),
                ('semestre', models.CharField(max_length=20)),
                ('specialité', models.CharField(max_length=20)),
                ('responsable', models.ForeignKey(to='services.Enseignant')),
            ],
        ),
        migrations.AddField(
            model_name='tache',
            name='ue',
            field=models.ForeignKey(to='services.Ue'),
        ),
    ]
