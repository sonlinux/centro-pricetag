# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'

from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField
from django.utils import timezone

PARTNER_CHOICES = (
    ('PT', 'PARTNER'),
    ('SP', 'SPONSOR'),
    ('OT', 'OTHER'),
)

SPONSOR_LEVEL_CHOICES = (
    ('GOLD', 'GOLD'),
    ('SILVER', 'SILVER'),
    ('BRONZE', 'BRONZE'),
)

class Partner(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    url = models.URLField(
        _('Website URL'),
        blank=True,
        null=True
    )
    contact_title = models.CharField(
        _('Sponsorship Representative Title'),
        max_length=255,
        null=True,
        blank=True,
        help_text=_('Title of the sponsorship representative i.e Treasurer.')
    )
    start_date = models.DateField(
        help_text='Sponsor start date.',
        default=timezone.now
    )
    end_date = models.DateField(
        help_text='Sponsor end date.',
        default=timezone.now
    )

    contact_person = models.CharField(
        help_text='Input the contact person of sponsor.',
        max_length=255,
        null=True,
        blank=True)

    address = models.TextField(
        help_text=(
            'Enter the complete street address for this sponsor. '
            'Use line breaks to separate address elements and use '
            'the country field to specify the country.'
        ),
        null=True,
        blank=True)

    country = CountryField(
        help_text='Select the country for this sponsor',
        blank_label='(Select country)',
        null=True,
        blank=True)

    sponsor_email = models.EmailField(
        help_text='Input an email of sponsor.',
        null=True,
        blank=True,
    )

    description = RichTextField(
        _('Description'),
        blank=True,
        null=True
    )

    partner_type = models.CharField(
        _('Type'),
        max_length=255,
        blank=True,
        null=True,
        choices=PARTNER_CHOICES
    )
    logo = models.ImageField(
        _('Logo'),
        null=True,
        blank=True,
        upload_to='partner/logos/%Y/%m/%d'
    )
    level = models.CharField(
        _('Sponsor level'),
        max_length=255,
        blank=True,
        null=True,
        choices=SPONSOR_LEVEL_CHOICES
    )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
