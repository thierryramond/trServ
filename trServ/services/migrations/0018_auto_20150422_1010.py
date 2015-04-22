# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_auto_20150419_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='millesime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tache',
            name='millesime',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='millesime',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
