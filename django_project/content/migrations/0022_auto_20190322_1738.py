# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0021_auto_20190322_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsummery',
            name='content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='What user will quickly read on home page summery about SmartCare', blank=True),
        ),
        migrations.AlterField(
            model_name='projectsummery',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Summery Title', blank=True),
        ),
    ]
