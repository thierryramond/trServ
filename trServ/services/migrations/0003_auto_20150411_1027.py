# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_tache_modifié_le'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='decharge',
            field=models.IntegerField(default=0),
        ),
    ]
