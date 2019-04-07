# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0025_auto_20190322_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Hub Name', blank=True)),
                ('content', ckeditor.fields.RichTextField(null=True, verbose_name='Details about this Hub that you want to share with public.', blank=True)),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Hub',
                'verbose_name_plural': 'Hubs',
            },
        ),
    ]
