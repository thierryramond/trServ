# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0022_auto_20150422_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='horaire_eqtd',
            field=models.IntegerField(blank=True),
        ),
    ]
