# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('isbn', models.CharField(max_length=13)),
                ('titulo', models.CharField(max_length=200)),
                ('anio', models.CharField(max_length=5)),
                ('estado', models.CharField(max_length=200)),
                ('autor', models.ForeignKey(to='libros.Autor', null=True, blank=True)),
                ('editorial', models.ForeignKey(to='libros.Editorial', null=True, blank=True)),
                ('pais', models.ForeignKey(to='libros.Pais', null=True, blank=True)),
                ('prestamista', models.ForeignKey(to='libros.Usuario', null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='post',
            name='editorial',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='post',
            name='prestamista',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
