# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'


# coding=utf-8
"""Carousel header model definition.

"""

from django.db import models
from ordered_model.models import OrderedModel


class CarouselHeader(OrderedModel):
    """Carousel header model."""

    banner = models.ImageField(
        upload_to='banner'
    )

    description = models.TextField(
        blank=True,
        default='',
    )

    def __str__(self):
        return self.description