# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_auto_20190321_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='successstory',
            name='photo_5',
        ),
        migrations.AlterField(
            model_name='successstory',
            name='photo_2',
            field=models.ImageField(upload_to=b'success_stories/upload/%Y/%m/%d', null=True, verbose_name='Story Optional photo 2', blank=True),
        ),
    ]
