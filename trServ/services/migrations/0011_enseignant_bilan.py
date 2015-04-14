# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20150413_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='bilan',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
