# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_foreword_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Author Name')),
                ('extra_info', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SuccessStory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Story Title')),
                ('content', ckeditor.fields.RichTextField()),
                ('photo', models.ImageField(upload_to=b'success_stories/upload/%Y/%m/%d', verbose_name='Story Image')),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.SET_DEFAULT, default=b'', to='content.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.SET_DEFAULT, default=b'', to='content.Category')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Success Story',
                'verbose_name_plural': 'Success Strories',
            },
        ),
    ]
