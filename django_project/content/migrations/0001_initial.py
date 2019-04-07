# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='smartcare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=350, null=True, verbose_name='Product Identifier', blank=True)),
                ('name', models.CharField(max_length=350, null=True, verbose_name='Product Name', blank=True)),
                ('brand', models.CharField(max_length=350, null=True, verbose_name='Brand Name', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Catalog Data',
                'verbose_name_plural': 'Catalog Data',
            },
        ),
    ]
