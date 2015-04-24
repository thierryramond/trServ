# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0020_auto_20150422_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ue',
            old_name='specialité',
            new_name='spécialité',
        ),
    ]
