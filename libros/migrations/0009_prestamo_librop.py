# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0008_remove_prestamo_librop'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='librop',
            field=models.ManyToManyField(to='libros.Libro', through='libros.Detalle'),
        ),
    ]
