# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gears', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GearProperties',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('mandatory', models.BooleanField()),
                ('input_type', models.IntegerField(choices=[(0, 'String'), (1, 'Integer'), (2, 'Float')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gear', models.ForeignKey(to='gears.Gear')),
            ],
        ),
    ]
