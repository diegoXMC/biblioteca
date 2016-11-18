# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nombreA', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nombreE', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nombreP', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('isbn', models.CharField(max_length=13)),
                ('titulo', models.CharField(max_length=200)),
                ('portada', models.TextField()),
                ('anio', models.CharField(max_length=5)),
                ('estado', models.CharField(max_length=200)),
                ('autor', models.ForeignKey(null=True, blank=True, to='libros.Autor')),
                ('editorial', models.ForeignKey(null=True, blank=True, to='libros.Editorial')),
                ('pais', models.ForeignKey(null=True, blank=True, to='libros.Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dpi', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='prestamista',
            field=models.ForeignKey(null=True, blank=True, to='libros.Usuario'),
        ),
    ]
