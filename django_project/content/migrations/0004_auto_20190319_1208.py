# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import ckeditor.fields
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20190319_1131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foreword',
            options={'verbose_name': 'Foreword', 'verbose_name_plural': 'Foreword Entries'},
        ),
        migrations.AddField(
            model_name='foreword',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='foreword',
            name='content',
            field=ckeditor.fields.RichTextField(default=b''),
        ),
        migrations.AddField(
            model_name='foreword',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foreword',
            name='owner',
            field=models.CharField(max_length=255, null=True, verbose_name='Foreword by', blank=True),
        ),
        migrations.AddField(
            model_name='foreword',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Foreword title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foreword',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 10, 8, 8, 224494, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='content',
            field=ckeditor.fields.RichTextField(default=b''),
        ),
    ]
