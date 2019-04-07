# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0018_auto_20190322_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='level',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Sponsor level', choices=[(b'GOLD', b'GOLD'), (b'SILVER', b'SILVER'), (b'BRONZE', b'BRONZE')]),
        ),
    ]
