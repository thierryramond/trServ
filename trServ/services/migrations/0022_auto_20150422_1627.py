# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_auto_20150422_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='commentaire',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
