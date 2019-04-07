# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20190319_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('logo', models.ImageField(upload_to=b'partner/logos/%Y/%m/%d', null=True, verbose_name='Logo', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='successstory',
            options={'ordering': ['-created'], 'verbose_name': 'Success Story', 'verbose_name_plural': 'Success Strories'},
        ),
    ]
