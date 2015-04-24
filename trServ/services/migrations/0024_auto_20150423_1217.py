# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0023_auto_20150422_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='nature',
            field=models.CharField(choices=[('TD', 'TD'), ('Cours', 'Cours'), ('Intégré', 'Intégré'), ('TP', 'TP')], max_length=20),
        ),
    ]
