# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_carouselheader'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='description',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='url',
            field=models.URLField(null=True, verbose_name='Website URL', blank=True),
        ),
    ]
