# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0026_auto_20150424_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='arrivé_en',
            field=models.DateField(default='2000-09-01'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='millesime',
            field=models.IntegerField(default=2015),
        ),
    ]
