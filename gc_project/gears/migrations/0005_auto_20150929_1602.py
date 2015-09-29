# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('gears', '0004_auto_20150929_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gearimage',
            name='photo',
            field=models.ImageField(upload_to='', storage=django.core.files.storage.FileSystemStorage(location='/home/vagrant/geo_project/gearcircles/gc_project/gears/static/gears/img')),
        ),
    ]
