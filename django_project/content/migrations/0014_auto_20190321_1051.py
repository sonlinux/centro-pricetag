# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_auto_20190321_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='functionalmodules',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overview',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
