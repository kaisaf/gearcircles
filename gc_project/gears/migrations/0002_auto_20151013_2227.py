# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('gears', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gearimage',
            name='photo',
            field=models.ImageField(upload_to='', storage=django.core.files.storage.FileSystemStorage(location='/home/vagrant/project/gc_project/gears/static/gears/img')),
        ),
    ]
