# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_enseignant_bilan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseignant',
            name='bilan',
        ),
        migrations.AddField(
            model_name='ue',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
