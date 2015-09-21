# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gears', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='payment',
            field=models.IntegerField(choices=[(0, 'Cash'), (1, 'Paypal'), (2, 'Any')]),
        ),
    ]
