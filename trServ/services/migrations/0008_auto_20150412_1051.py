# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20150412_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='ue',
            name='horaire_coordination',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='horaire_soutien',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='nombre_cours',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='nombre_intégré',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='nombre_soutien',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='nombre_td',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='nombre_tp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
