# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_auto_20150422_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ue',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
