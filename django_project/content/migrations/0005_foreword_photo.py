# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20190319_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreword',
            name='photo',
            field=models.ImageField(upload_to=b'photos/', null=True, verbose_name="Owner's Picture", blank=True),
        ),
    ]
