# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.FloatField(blank=True),
        ),
    ]
