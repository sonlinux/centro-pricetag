# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20190319_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselHeader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('banner', models.ImageField(upload_to=b'banner')),
                ('description', models.TextField(default=b'', blank=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
