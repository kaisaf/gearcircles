# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150922_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
