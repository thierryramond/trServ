# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20150412_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='horaire_eqtd',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tache',
            name='horaire_reel',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
