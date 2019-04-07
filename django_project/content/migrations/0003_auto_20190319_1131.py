# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_aboutus_foreword'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
