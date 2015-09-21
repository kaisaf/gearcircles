# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gears', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price_paid', models.FloatField()),
                ('payment_method', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('borrower_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='transactions_borrowed')),
                ('gear', models.ForeignKey(to='gears.Gear')),
                ('owner_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='transactions_owned')),
            ],
        ),
    ]
