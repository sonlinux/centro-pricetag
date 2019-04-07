# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_auto_20190322_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='sponsor_url',
        ),
        migrations.AddField(
            model_name='partner',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, help_text=b'Sponsor end date.'),
        ),
        migrations.AddField(
            model_name='partner',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, help_text=b'Sponsor start date.'),
        ),
    ]
