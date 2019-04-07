# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0023_auto_20190322_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectsummery',
            options={'ordering': ['created'], 'verbose_name': 'Summery', 'verbose_name_plural': 'Summeries'},
        ),
        migrations.AddField(
            model_name='projectsummery',
            name='active_on_site',
            field=models.BooleanField(default=True, verbose_name='Is it the one you want to use on the home page?'),
        ),
    ]
