# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_auto_20150422_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='millesime',
            field=models.IntegerField(default=2015),
        ),
    ]
