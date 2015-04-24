# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_auto_20150423_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='horaire_eqtd',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
