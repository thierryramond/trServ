# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_auto_20150418_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='arrivé_en',
            field=models.DateField(default='1970-01-01'),
        ),
    ]
