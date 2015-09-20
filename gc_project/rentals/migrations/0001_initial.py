# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gears', '0003_gearavailability_gearimage'),
        ('users', '0003_remove_user_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price_paid', models.FloatField()),
                ('payment_method', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('borrower_user', models.ForeignKey(to='users.User', related_name='transactions_borrowed')),
                ('gear', models.ForeignKey(to='gears.Gear')),
                ('owner_user', models.ForeignKey(to='users.User', related_name='transactions_owned')),
            ],
        ),
    ]
