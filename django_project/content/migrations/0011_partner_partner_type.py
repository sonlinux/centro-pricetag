# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20190319_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='partner_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Type', choices=[(b'PT', b'PARTNER'), (b'SP', b'SPONSOR')]),
        ),
    ]
