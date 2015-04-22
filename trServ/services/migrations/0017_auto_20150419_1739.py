# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_auto_20150418_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='depuis',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='arrivé_en',
            field=models.DateField(blank=True),
        ),
    ]
