# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13)),
                ('titulo', models.CharField(max_length=200)),
                ('anio', models.CharField(max_length=5)),
                ('autor', models.ForeignKey(to='libros.Autor', blank=True, null=True)),
                ('editorial', models.ForeignKey(to='libros.Editorial', blank=True, null=True)),
                ('pais', models.ForeignKey(to='libros.Pais', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idprestamo', models.CharField(max_length=200)),
                ('fechaI', models.DateTimeField(null=True, blank=True)),
                ('fechaF', models.DateTimeField(null=True, blank=True)),
                ('librop', models.ManyToManyField(through='libros.Detalle', to='libros.Libro')),
                ('usuariop', models.ForeignKey(to='libros.Usuario', blank=True, null=True)),
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
        migrations.AddField(
            model_name='detalle',
            name='librop',
            field=models.ForeignKey(to='libros.Libro'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='prestamop',
            field=models.ForeignKey(to='libros.Prestamo'),
        ),
    ]
