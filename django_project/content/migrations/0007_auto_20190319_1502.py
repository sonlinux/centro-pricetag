# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_author_category_successstory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='photo',
            field=models.ImageField(upload_to=b'success_stories/upload/%Y/%m/%d', null=True, verbose_name='Story Image', blank=True),
        ),
    ]
