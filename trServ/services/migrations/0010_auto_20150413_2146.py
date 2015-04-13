# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20150413_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tache',
            old_name='enseignant',
            new_name='attribué_à',
        ),
    ]
