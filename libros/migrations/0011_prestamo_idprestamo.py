# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0010_auto_20161118_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='idprestamo',
            field=models.CharField(default=datetime.datetime(2016, 11, 18, 17, 37, 56, 674017, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
