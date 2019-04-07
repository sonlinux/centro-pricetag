# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0024_auto_20190322_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsummery',
            name='active_on_site',
            field=models.BooleanField(default=False, verbose_name='Is it the one you want to use on the home page?'),
        ),
    ]
