# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20150411_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='ue',
            name='horaire_cours',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='horaire_intégré',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='horaire_td',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='horaire_total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='horaire_tp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
