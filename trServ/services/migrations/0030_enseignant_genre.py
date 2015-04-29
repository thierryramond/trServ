# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0029_auto_20150428_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='genre',
            field=models.CharField(default='M', max_length=10, choices=[('M', 'M'), ('Mme', 'Mme')]),
            preserve_default=False,
        ),
    ]
