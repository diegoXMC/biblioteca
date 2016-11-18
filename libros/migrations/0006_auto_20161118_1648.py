# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0005_prestamo_fechaf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('librop', models.ForeignKey(blank=True, null=True, to='libros.Libro')),
            ],
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='librop',
        ),
        migrations.AddField(
            model_name='detalle',
            name='prestamop',
            field=models.ForeignKey(blank=True, null=True, to='libros.Prestamo'),
        ),
    ]
