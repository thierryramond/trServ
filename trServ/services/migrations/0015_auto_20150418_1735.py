# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20150418_1359'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enseignant',
            unique_together=set([('nom', 'prenom')]),
        ),
    ]
