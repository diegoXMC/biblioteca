# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0004_prestamo_fechai'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='fechaF',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
