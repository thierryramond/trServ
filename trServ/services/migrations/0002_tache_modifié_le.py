# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='modifié_le',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 4, 11, 8, 16, 54, 629873, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
