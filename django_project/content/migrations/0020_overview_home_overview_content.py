# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0019_partner_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='overview',
            name='home_overview_content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='What user will see on home page summery about SmartCare', blank=True),
        ),
    ]
