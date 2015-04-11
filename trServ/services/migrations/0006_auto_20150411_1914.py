# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20150411_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='commentaire',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='photo',
            field=models.ImageField(upload_to='', blank=True),
        ),
    ]
