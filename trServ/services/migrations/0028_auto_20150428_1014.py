# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0027_auto_20150425_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='horaire_eqtd',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ue',
            name='année',
            field=models.CharField(choices=[('00', '00'), ('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3'), ('M1', 'M1'), ('M2', 'M2'), ('D', 'D')], max_length=20),
        ),
        migrations.AlterField(
            model_name='ue',
            name='description',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ue',
            name='horaire_coordination',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='horaire_cours',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='horaire_intégré',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='horaire_soutien',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='horaire_td',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='horaire_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='horaire_tp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='millesime',
            field=models.IntegerField(default=2015),
        ),
        migrations.AlterField(
            model_name='ue',
            name='nombre_cours',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='nombre_intégré',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='nombre_soutien',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='nombre_td',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='nombre_tp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='semestre',
            field=models.CharField(choices=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6')], max_length=20),
        ),
        migrations.AlterField(
            model_name='ue',
            name='spécialité',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
    ]
