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


class Category(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )

    description = RichTextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name