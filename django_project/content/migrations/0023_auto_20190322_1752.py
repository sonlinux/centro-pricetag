# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0022_auto_20190322_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsummery',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
