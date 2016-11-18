# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_auto_20161118_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('librop', models.ForeignKey(blank=True, to='libros.Libro', null=True)),
                ('usuariop', models.ForeignKey(blank=True, to='libros.Usuario', null=True)),
            ],
        ),
    ]
