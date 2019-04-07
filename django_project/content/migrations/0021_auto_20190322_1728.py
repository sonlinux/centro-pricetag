# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0020_overview_home_overview_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectSummery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', ckeditor.fields.RichTextField(null=True, verbose_name='What user will see on home page summery about SmartCare', blank=True)),
                ('published', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='overview',
            name='home_overview_content',
        ),
    ]
