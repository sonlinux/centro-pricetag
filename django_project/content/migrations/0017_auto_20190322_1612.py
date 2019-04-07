# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_auto_20190321_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='address',
            field=models.TextField(help_text=b'Enter the complete street address for this sponsor. Use line breaks to separate address elements and use the country field to specify the country.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='contact_person',
            field=models.CharField(help_text=b'Input the contact person of sponsor.', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='contact_title',
            field=models.CharField(help_text='Title of the sponsorship representative i.e Treasurer.', max_length=255, null=True, verbose_name='Sponsorship Representative Title', blank=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, help_text=b'Select the country for this sponsor'),
        ),
        migrations.AddField(
            model_name='partner',
            name='sponsor_email',
            field=models.EmailField(help_text=b'Input an email of sponsor.', max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='sponsor_url',
            field=models.CharField(help_text=b'Input the sponsor URL.', max_length=255, null=True, blank=True),
        ),
    ]
