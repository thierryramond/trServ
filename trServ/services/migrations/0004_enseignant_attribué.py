# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20150411_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='attribué',
            field=models.IntegerField(default=0),
        ),
    ]
