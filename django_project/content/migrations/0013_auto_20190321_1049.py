# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20190321_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='developmentpipeline',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='technicalupdates',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='technologystack',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='training',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
