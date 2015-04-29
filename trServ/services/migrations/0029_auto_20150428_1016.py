# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0028_auto_20150428_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='attribué',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='bilan',
            field=models.FloatField(default=0),
        ),
    ]
