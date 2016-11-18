# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0006_auto_20161118_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='librop',
            field=models.ForeignKey(to='libros.Libro', null=True, blank=True),
        ),
    ]
