# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_auto_20190321_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstory',
            name='photo_1',
            field=models.ImageField(upload_to=b'success_stories/upload/%Y/%m/%d', null=True, verbose_name='Story Optional photo 1', blank=True),
        ),
        migrations.AddField(
            model_name='successstory',
            name='photo_2',
            field=models.ImageField(upload_to=b'success_stories/upload/%Y/%m/%d', null=True, verbose_name='Story Main Optional photo 2', blank=True),
        ),
        migrations.AddField(
            model_name='successstory',
            name='photo_3',
            field=models.ImageField(upload_to=b'success_stories/upload/%Y/%m/%d', null=True, verbose_name='Story Optional photo 3', blank=True),
        ),
        migrations.AddField(
            model_name='successstory',
            name='photo_4',
            field=models.ImageField(upload_to=b'success_stories/upload/%Y/%m/%d', null=True, verbose_name='Story Optional photo 4', blank=True),
        ),
        migrations.AddField(
            model_name='successstory',
            name='photo_5',
            field=models.ImageField(upload_to=b'success_stories/upload/%Y/%m/%d', null=True, verbose_name='Story Optional photo 5', blank=True),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='photo',
            field=models.ImageField(upload_to=b'success_stories/upload/%Y/%m/%d', null=True, verbose_name='Story Main Photo', blank=True),
        ),
    ]
