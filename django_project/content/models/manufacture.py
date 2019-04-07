# coding: utf-8
__author__ = 'Alison Mukoma <alison@devsbranch.com>'
__license__ = 'GPL'
__copyright__ = 'devsbranch.com'

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_countries.fields import CountryField


class Manufacture(models.Model):
    name = models.CharField(
        _('Manufacture Name'),
        max_length=255,
        null=True,
        blank=True,
    )
    country = CountryField(blank_label='(select country)')

    def __str__(self):
        return self.name
