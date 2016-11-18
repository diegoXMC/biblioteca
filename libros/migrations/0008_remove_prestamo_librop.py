# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0007_prestamo_librop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamo',
            name='librop',
        ),
    ]
