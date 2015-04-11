# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_enseignant_attribué'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='arrivé_en',
            field=models.DateField(default=datetime.datetime(2015, 4, 11, 13, 8, 17, 489104, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enseignant',
            name='commentaire',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enseignant',
            name='photo',
            field=models.ImageField(upload_to='', default=''),
            preserve_default=False,
        ),
    ]
