# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gears', '0003_auto_20150928_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryproperty',
            name='categories',
        ),
        migrations.AddField(
            model_name='categoryproperty',
            name='category',
            field=models.ForeignKey(to='gears.Category', default=1),
            preserve_default=False,
        ),
    ]
