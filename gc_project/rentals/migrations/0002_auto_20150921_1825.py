# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_method',
            field=models.IntegerField(choices=[(0, 'Cash'), (1, 'Paypal')]),
        ),
    ]
