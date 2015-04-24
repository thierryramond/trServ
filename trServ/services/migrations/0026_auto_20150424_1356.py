# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0025_auto_20150423_1923'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enseignant',
            unique_together=set([('nom', 'prenom', 'millesime')]),
        ),
        migrations.AlterUniqueTogether(
            name='ue',
            unique_together=set([('code', 'millesime')]),
        ),
    ]
