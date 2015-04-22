# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_enseignant_bilan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='bilan',
            field=models.IntegerField(default=0),
        ),
    ]
