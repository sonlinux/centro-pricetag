# coding: utf-8
__author__ = 'Alison Mukoma <alison@devsbranch.com>'
__license__ = 'GPL'
__copyright__ = 'devsbranch.com'

import os
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf.global_settings import MEDIA_ROOT
from .category import Category
from .location import Location
from .manufacture import Manufacture
from .shop_owner import ShopOwner
from djmoney.models.fields import MoneyField


class Product(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
        null=False,
        blank=False
    )
    code = models.CharField(
        _('Product Code'),
        max_length=255,
        null=True,
        blank=True
    )
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='ZMK',
        max_digits=11,
    )
    specifications = models.TextField(
        _('Specifications'),
        null=True,
        blank=True
    )
    description = models.TextField(
        _('Description'),
        null=True,
        blank=True,
    )
    is_available = models.BooleanField(
        _('Is product in stock?'),
        default=True
    )

    shop = models.ForeignKey(
        ShopOwner,
        on_delete=models.CASCADE,
        default=''
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    manufacture = models.ForeignKey(
        Manufacture,
        on_delete=models.CASCADE
    )
    photo_main = models.ImageField(
        _("Main Image"),
        upload_to=os.path.join(
            MEDIA_ROOT, 'photos/vendors/products/%Y/%m/%d/'),
        default=''
    )
    photo_1 = models.ImageField(
        _("Image 1"),
        upload_to=os.path.join(
            MEDIA_ROOT, 'photos/vendors/products/%Y/%m/%d/'),
        blank=True
    )
    photo_2 = models.ImageField(
        _("Image 2"),
        upload_to=os.path.join(
            MEDIA_ROOT, 'photos/vendors/products/%Y/%m/%d/'),
        blank=True
    )
    photo_3 = models.ImageField(
        _("Image 3"),
        upload_to=os.path.join(
            MEDIA_ROOT, 'photos/vendors/products/%Y/%m/%d/'),
        blank=True
    )
    photo_4 = models.ImageField(
        _("Image 4"),
        upload_to=os.path.join(
            MEDIA_ROOT, 'photos/vendors/products/%Y/%m/%d/'),
        blank=True
    )
    photo_5 = models.ImageField(
        _("Image 5"),
        upload_to=os.path.join(
            MEDIA_ROOT, 'photos/vendors/products/%Y/%m/%d/'),
        blank=True
    )
    photo_6 = models.ImageField(
        _("Image 6"),
        upload_to=os.path.join(
            MEDIA_ROOT, 'photos/vendors/products/%Y/%m/%d/'),
        blank=True
    )
    created = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['id', 'created']

    def __str__(self):
        return self.name
