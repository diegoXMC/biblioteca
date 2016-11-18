# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_prestamo'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='fechaI',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
